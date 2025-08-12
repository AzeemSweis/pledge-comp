import csv

def read_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Create a dictionary only for rows with numeric amounts
        return {rows[0]: float(rows[1]) for rows in reader if rows[1].replace('.', '', 1).isdigit()}

def compare_pledges(previous_month_file, current_month_file):
    previous_month = read_csv(previous_month_file)
    current_month = read_csv(current_month_file)

    # Check for new entries and changes in the amount
    for name, amount in current_month.items():
        if name not in previous_month:
            print(f"New pledge: {name} with amount {amount}")
        elif previous_month[name] != amount:
            print(f"Updated pledge for {name}: New amount {amount}")

    # Check for deleted entries
    for name in previous_month:
        if name not in current_month:
            print(f"Delete pledge for {name}")

# Example usage
previous_month = input("Enter the path of the previous month's CSV file: ")
current_month = input("Enter the path of the new month's CSV file: ")
compare_pledges(previous_month, current_month)
