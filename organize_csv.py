import csv

def organize_csv(file_path):
    # Read the CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Sort the data by the first name in the name column
    sorted_data = sorted(data[1:], key=lambda x: x[0].split()[0])

    # Write the sorted data back to the CSV file
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([data[0]] + sorted_data)

# Usage example
file_path = input("Enter the CSV file name: ")
organize_csv(file_path)
