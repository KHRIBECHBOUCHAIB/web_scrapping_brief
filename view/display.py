# view/display.py

import tkinter as tk
from tkinter import ttk

def display_jobs_gui(jobs):
    # Create a new window
    window = tk.Tk()
    window.title("Job Listings")

    # Set up the treeview widget to display job listings in a table format
    tree = ttk.Treeview(window)
    tree['columns'] = ('Job Title', 'Company', 'Location')

    # Define columns
    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('Job Title', anchor=tk.W, width=200)
    tree.column('Company', anchor=tk.W, width=150)
    tree.column('Location', anchor=tk.W, width=150)

    # Define column headings
    tree.heading('#0', text='', anchor=tk.W)
    tree.heading('Job Title', text='Job Title', anchor=tk.W)
    tree.heading('Company', text='Company', anchor=tk.W)
    tree.heading('Location', text='Location', anchor=tk.W)

    # Insert job listings
    for job in jobs:
        tree.insert('', tk.END, values=(job.title, job.company, job.location))

    # Pack the treeview widget
    tree.pack(pady=20, padx=20)

    # Run the main loop
    window.mainloop()
