# main.py
# Author: Khribech Bouchaib
# Version: 1.2
# Project: Job Listings Web Scraper - MVC Project
# Description: Entry point for scraping job listings, displaying them using a Tkinter GUI, and converting to Pandas DataFrame.
# Formation: Simplon AI Developer Certification

import pandas as pd  # Import pandas for DataFrame operations
from controller.scraper import scrape_jobs  # Import scraping function
from view.display import display_jobs_gui  # Import GUI display function

def main():
    # Base URL for the website to scrape
    base_url = "https://realpython.github.io/fake-jobs/"
    
    # Scrape jobs from the given URL
    jobs = scrape_jobs(base_url)

    # Display the scraped jobs using Tkinter GUI if there are jobs available
    if jobs:
        # Convert jobs to Pandas DataFrame
        jobs_data = [
            {
                'Job Title': job.title,
                'Company': job.company,
                'Location': job.location,
                'Link': job.link,
                'Description': job.description,
                'Skills': ', '.join(job.skills)
            }
            for job in jobs
        ]

        # Create DataFrame from list of dictionaries
        df_jobs = pd.DataFrame(jobs_data)

        # Print the DataFrame to verify the data
        print(df_jobs)

        # Optionally, save to CSV
        df_jobs.to_csv('scraped_jobs.csv', index=False)
        print("Data saved to scraped_jobs.csv")

        # Display jobs in the GUI
        display_jobs_gui(jobs)
    else:
        print("No jobs found or an error occurred while scraping.")

# Entry point for the script
if __name__ == "__main__":
    main()
