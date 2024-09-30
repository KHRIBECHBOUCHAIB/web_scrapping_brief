# controller/scraper.py

import requests
from bs4 import BeautifulSoup
from model.data_model import Job

def scrape_jobs(url):
    # Step 1: Get the HTML Content
    page = requests.get(url)
    if page.status_code != 200:
        print(f"Failed to retrieve page, status code: {page.status_code}")
        return []

    # Step 2: Parse the HTML Content with BeautifulSoup and html5lib
    soup = BeautifulSoup(page.content, 'html5lib')

    # Step 3: Find All Job Listings
    job_elements = soup.find_all('div', class_='card-content')

    # Step 4: Extract Information into Job Objects
    jobs = []
    for job_element in job_elements:
        title_element = job_element.find('h2', class_='title')
        company_element = job_element.find('h3', class_='company')
        location_element = job_element.find('p', class_='location')
        
        # Create Job object if all elements are found
        if title_element and company_element and location_element:
            job = Job(
                title=title_element.text.strip(),
                company=company_element.text.strip(),
                location=location_element.text.strip()
            )
            jobs.append(job)
    
    return jobs
