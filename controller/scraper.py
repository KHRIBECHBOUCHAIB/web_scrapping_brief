# scraper.py
# Author: Khribech Bouchaib
# Version: 1.3
# Project: Job Listings Web Scraper - MVC Project
# Description: Web scraping controller that extracts job listings using requests and Beautiful Soup.
# Formation: Simplon AI Developer Certification

import requests
from bs4 import BeautifulSoup
from model.data_model import Job
import time

# Helper function to get page content
def get_page_content(url):
    try:
        page = requests.get(url, timeout=10)
        page.raise_for_status()
        return page.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page content from {url}: {e}")
        return None

# Function to extract job data from the main page job element
def extract_job_data(job_element):
    title_element = job_element.find('h2', class_='title')
    company_element = job_element.find('h3', class_='company')
    location_element = job_element.find('p', class_='location')
    link_element = job_element.find('a', class_='card-footer-item', string="Apply")

    if title_element and company_element and location_element and link_element:
        job = Job(
            title=title_element.text.strip(),
            company=company_element.text.strip(),
            location=location_element.text.strip(),
            link=link_element.get('href')
        )
        # Fetch detailed job description from the individual job page
        job = scrape_job_details(job)
        return job
    return None

# Function to scrape the detailed job page
def scrape_job_details(job):
    if job.link:
        job_page_content = get_page_content(job.link)
        if job_page_content is None:
            return job

        soup = BeautifulSoup(job_page_content, 'html5lib')

        # Extract detailed job information
        description_element = soup.find('div', class_='description') or soup.find('div', class_='content')
        if description_element:
            job.description = description_element.get_text(strip=True)

        # Extract other details if needed (e.g., requirements, responsibilities, etc.)
        skills_list = soup.find('ul', class_='skills-list')
        if skills_list:
            job.skills = [skill.get_text(strip=True) for skill in skills_list.find_all('li')]

    return job

# Function to scrape all jobs from the main page
def scrape_jobs(url):
    page_content = get_page_content(url)
    if page_content is None:
        return []

    soup = BeautifulSoup(page_content, 'html5lib')
    job_elements = soup.find_all('div', class_='card-content')

    jobs = []
    for job_element in job_elements:
        job = extract_job_data(job_element)
        if job:
            jobs.append(job)

    return jobs
