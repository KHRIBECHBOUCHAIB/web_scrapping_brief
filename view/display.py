# view/display.py
# Author: Khribech Bouchaib
# Version: 1.3
# Project: Job Listings Web Scraper - MVC Project
# Description: GUI for displaying job listings using Tkinter.
# Formation: Simplon AI Developer Certification

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser

def display_jobs_gui(jobs):
    # Create a new window
    window = tk.Tk()
    window.title("Job Listings")
    window.geometry("1000x600")

    # Set up the treeview widget to display job listings in a table format
    tree = ttk.Treeview(window, columns=('Job Title', 'Company', 'Location', 'Link', 'Description', 'Skills'), show='headings')
    tree.pack(pady=20, padx=20, fill='both', expand=True)

    # Define columns
    for column in tree['columns']:
        tree.heading(column, text=column, anchor=tk.W)
        tree.column(column, anchor=tk.W, width=200 if column == 'Job Title' else 150)

    # Insert job listings into the treeview
    for job in jobs:
        tree.insert('', tk.END, values=(
            job.title,
            job.company,
            job.location,
            job.link,
            job.description,
            ', '.join(job.skills)
        ))

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Button to show job details
    def show_job_details():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a job listing to view details.")
            return
        job_values = tree.item(selected_item, 'values')
        job_details = f"Job Title: {job_values[0]}\nCompany: {job_values[1]}\nLocation: {job_values[2]}\nLink: {job_values[3]}\nDescription: {job_values[4]}\nSkills: {job_values[5]}"
        messagebox.showinfo("Job Details", job_details)

    # Button to open the job link in a web browser
    def open_apply_link():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a job listing to apply.")
            return
        job_values = tree.item(selected_item, 'values')
        job_link = job_values[3]
        if job_link == "N/A":
            messagebox.showwarning("Link Error", "No valid link available for this job.")
        else:
            webbrowser.open(job_link)

    # Add buttons for job details and applying
    details_button = tk.Button(window, text="Show Details", command=show_job_details)
    details_button.pack(pady=10)

    apply_button = tk.Button(window, text="Apply", command=open_apply_link)
    apply_button.pack(pady=5)

    # Run the main loop
    window.mainloop()
