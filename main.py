# main.py

from controller.scraper import scrape_jobs
from view.display import display_jobs_gui

def main():
    url = "https://realpython.github.io/fake-jobs/"
    jobs = scrape_jobs(url)
    display_jobs_gui(jobs)

if __name__ == "__main__":
    main()
