# main.py
# Author: Khribech Bouchaib
# Version: 1.1
# Project: Job Listings Web Scraper - MVC Project
# Description: Entry point for scraping job listings and displaying them using a Tkinter GUI.
# Formation: Simplon AI Developer Certification

from controller.scraper import scrape_jobs  # Import only scrape_jobs as we no longer use scrape_all_pages
from view.display import display_jobs_gui  # Import the GUI display function

def main():
    # Base URL for the website to scrape
    base_url = "https://realpython.github.io/fake-jobs/"
    
    # Scrape jobs from the given URL
    jobs = scrape_jobs(base_url)

    # Display the scraped jobs using Tkinter GUI
    if jobs:
        display_jobs_gui(jobs)
    else:
        print("No jobs found or an error occurred while scraping.")

# Entry point for the script
if __name__ == "__main__":
    main()