import csv
import pyttsx3

def read_second_column_aloud(csv_file, speech_rate=200):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Set properties like speech rate
    engine.setProperty('rate', speech_rate)  # Set the speech rate (default is around 200)

    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            
            for row in reader:
                try:
                    number = float(row[1])  # Convert the second column value to a number
                    print(f"Reading number: {number}")
                    engine.say(str(number))  # Say the number out loud
                    engine.runAndWait()
                except ValueError:
                    print(f"Skipping invalid data: {row[1]}")
    except FileNotFoundError:
        print(f"File {csv_file} not found.")

if __name__ == "__main__":
    csv_file_path = input("your_file.csv: ")   # Replace with your file path
    read_second_column_aloud(csv_file_path, speech_rate=400)  # Adjust the speech rate as desired
