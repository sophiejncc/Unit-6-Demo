import csv # built in csv library for python, different to pandas

# define the function to open, read and return as a list
def read_csv(filename: str):
    with open(filename, 'r') as file:
        file_reader = csv.reader(file)
        return list(file_reader)
