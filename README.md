# Web Scrapping Brief
# Job Listings Web Scraper - MVC Project

**Author**: Khribech Bouchaib  
**Version**: 1.0  
**Formation**: Simplon AI Developer Certification

## Overview

A Python-based web scraper for job listings using **Beautiful Soup**, **requests**, and **html5lib**. The project follows the **MVC** design pattern and displays results in a **Tkinter** GUI. 

## Features

- Extracts job data (title, company, location, skills).
- **MVC architecture** for modular code.
- GUI using **Tkinter** for job display.
- Save job data to **Excel**.

## Setup

1. **Clone**: `git clone https://github.com/KHRIBECHBOUCHAIB/web_scrapping_brief.git`
2. **Create Virtual Env**: `python -m venv venv`
3. **Activate Env**:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. **Install Dependencies**: `pip install -r requirements.txt`

## Usage

Run the main script to scrape job listings and display them in a GUI:
```sh
python main.py
