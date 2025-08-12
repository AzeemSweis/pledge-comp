import csv

def read_csv_to_dict(csv_file):
    """
    Reads the CSV file and returns a dictionary with the donor's name as the key
    and the donation amount as the value.
    """
    data = {}
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0].strip().lower()  # Standardize the name format (case insensitive)
                amount = float(row[1])
                data[name] = amount
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
    return data

def compare_donations(file1, file2):
    """
    Compares two donation CSV files and prints out the changes between them.
    """
    data1 = read_csv_to_dict(file1)  # Previous month
    data2 = read_csv_to_dict(file2)  # Current month

    added_donors = []
    removed_donors = []
    changed_donations = []

    # Check for added or updated donors
    for name, amount in data2.items():
        if name not in data1:
            added_donors.append((name, amount))
        elif data1[name] != amount:
            changed_donations.append((name, data1[name], amount))

    # Check for removed donors
    for name in data1:
        if name not in data2:
            removed_donors.append((name, data1[name]))

    # Output results
    print("Donors Added:")
    for name, amount in added_donors:
        print(f"{name.title()} added with a donation of {amount}")

    print("\nDonors Removed:")
    for name, amount in removed_donors:
        print(f"{name.title()} removed (previous donation: {amount})")

    print("\nDonors with Changed Donations:")
    for name, old_amount, new_amount in changed_donations:
        print(f"{name.title()} changed donation from {old_amount} to {new_amount}")

if __name__ == "__main__":
    previous_month_csv = input('previous_month.csv: ')  # Replace with previous month's file path
    current_month_csv = input('current_month.csv: ')    # Replace with current month's file path
    compare_donations(previous_month_csv, current_month_csv)
