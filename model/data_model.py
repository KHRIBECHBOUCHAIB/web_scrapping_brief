# model/data_model.py

class Job:
    def __init__(self, title, company, location):
        self.title = title
        self.company = company
        self.location = location

    def __str__(self):
        return f"Job Title: {self.title}\nCompany: {self.company}\nLocation: {self.location}\n" + ("-" * 40)
