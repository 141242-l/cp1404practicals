"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data(FILENAME)
    display_subject_details(data)


def load_data(filename=FILENAME):
    data_list = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data_list.append(parts)
    input_file.close()
    return data_list


def display_subject_details(data):
    for subject in data:
        code = subject[0]
        lecturer = subject[1]
        num_students = subject[2]
        print(f"{code} is taught by {lecturer:12} and has {num_students:3} students")


main()