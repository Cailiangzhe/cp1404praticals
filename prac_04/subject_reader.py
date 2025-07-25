"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    display_data(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    name_list = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        name_list.append(parts)
    input_file.close()
    return name_list

def display_data(data):
    for detail in data:
        subject = detail[0]
        lecturer = detail[1]
        total_students = detail[2]
        print(f"{subject} is taught by {lecturer} and has {total_students} students")

main()
