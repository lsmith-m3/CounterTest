import json
import time

# Path to the JSON file
json_file_path = 'counter.json'

# Function to read the current number from the JSON file
def read_current_number():
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        return data['current_number']

# Function to update the number in the JSON file
def update_number_in_json(new_number):
    with open(json_file_path, 'w') as file:
        json.dump({"current_number": new_number}, file)

# Infinite loop to increment the number every 30 seconds
while True:
    # Read the current number from JSON
    current_number = read_current_number()
    
    # Increase the number by 10
    new_number = current_number + 10
    
    # Print the new number
    print(f"Updated number: {new_number}")
    
    # Update the JSON file with the new number
    update_number_in_json(new_number)
    
    # Wait for 30 seconds before repeating
    time.sleep(30)
