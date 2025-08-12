import csv

def sum_second_column(csv_file):
    total = 0
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    total += float(row[1])  # Convert the second column value to float and add to total
                except ValueError:
                    print(f"Skipping invalid data: {row[1]}")
        return total
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
        return None

if __name__ == "__main__":
    csv_file_path = input("What file bitch: ")  # Replace with your file path
    result = sum_second_column(csv_file_path)
    if result is not None:
        print(f"Total sum of the second column: {result}")
