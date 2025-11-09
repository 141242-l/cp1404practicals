from project import Project
from datetime import datetime

FILENAME = "projects.txt"

def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 5:
                name, start_date, priority, cost, completion = parts
                projects.append(Project(name, start_date, int(priority), float(cost), int(completion)))
    return projects