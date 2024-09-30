# model/data_model.py
# Author: Khribech Bouchaib
# Version: 1.1
# Project: Job Listings Web Scraper - MVC Project
# Description: Data model representing a job listing.
# Formation: Simplon AI Developer Certification

class Job:
    def __init__(self, title, company, location, link=None, description=None, skills=None):
        self.title = title or "N/A"
        self.company = company or "N/A"
        self.location = location or "N/A"
        self.link = link or "N/A"
        self.description = description or "N/A"
        self.skills = skills if skills else []

    def __str__(self):
        job_details = f"Job Title: {self.title}\nCompany: {self.company}\nLocation: {self.location}\n"
        if self.link != "N/A":
            job_details += f"Link: {self.link}\n"
        if self.description != "N/A":
            job_details += f"Description: {self.description}\n"
        if self.skills:
            job_details += "Skills Required:\n" + "\n".join([f"- {skill}" for skill in self.skills]) + "\n"
        job_details += "-" * 40
        return job_details
