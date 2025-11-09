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

def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for p in projects:
            file.write(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t{p.cost_estimate}\t{p.completion_percentage}\n")

def display_projects(projects):
    incomplete = []
    complete = []

    for project in projects:
        if project.is_complete():
            complete.append(project)
        else:
            incomplete.append(project)

    incomplete.sort()
    complete.sort()
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


