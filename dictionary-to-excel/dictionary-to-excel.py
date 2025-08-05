import pandas as pd
import os

def collect_data():
    data = {}
    
    while True:
        key = input("Enter key name (e.g., 'roll number'): ")
        
        try:
            count = int(input(f"How many values do you want to enter for '{key}'? "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        values = []
        for i in range(count):
            val = input(f"Enter value {i+1} for '{key}': ")
            values.append(val)
        
        data[key] = values

        more = input("Do you want to add another key? (yes/no): ").strip().lower()
        if more != 'yes':
            break

    return data

def save_to_excel(data_dict, filename="output.xlsx"):
    # Get path of the folder where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Combine with filename to get full path
    full_path = os.path.join(script_dir, filename)

    # Pad value lists to equal length
    max_len = max(len(v) for v in data_dict.values())
    for key in data_dict:
        while len(data_dict[key]) < max_len:
            data_dict[key].append("")

    df = pd.DataFrame(data_dict)
    
    try:
        df.to_excel(full_path, index=False)
        print(f"\n✅ Data saved to: {full_path}")
    except Exception as e:
        print(f"\n❌ Failed to save file. Error: {e}")

# Main
if __name__ == "__main__":
    user_data = collect_data()
    save_to_excel(user_data)
# This code collects user input to create a dictionary and saves it to an Excel file.
# It ensures that all lists in the dictionary are of equal length before saving.
r