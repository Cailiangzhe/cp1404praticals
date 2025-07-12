"""
Project Management Program
Estimated time: 2.5 hours
Actual time:  hours
"""

from project import Project
import datetime

FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    menu = "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
    choice = ""
    while choice.lower() != "q":
        print(menu)
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            pass
        elif choice == "d":
            pass
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            pass
        elif choice == "a":
            pass
        elif choice == "u":
            pass
        elif choice == "q":
            confirm = input(f"Would you like to save to {FILENAME}? ").lower()
            if confirm =="y" or confirm =="yes":
                pass
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    with open(filename,"r") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects



main()
