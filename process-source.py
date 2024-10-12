import pandas as pd
import os

# Load the Excel source file
excel_file = 'source-files/2024/cl-madrid/cl-madrid-2024-eliminatoria-original.xlsx'

# Define the destination folder for the CSV
csv_destination_folder = 'source-files/2024/cl-madrid/eliminatoria'

# Load all the sheets into a dictionary of DataFrames
all_sheets = pd.read_excel(excel_file, sheet_name=None)

# Loop through each sheet and save as a separate CSV
for sheet_name, df in all_sheets.items():
    # Save each sheet to a CSV file
    df.to_csv(f'{csv_destination_folder}/{sheet_name}.csv', index=False)

def rename_files_in_folder(folder_path):
    # Loop through all files in the given folder
    for filename in os.listdir(folder_path):
        # Construct full file path
        file_path = os.path.join(folder_path, filename)
        
        # Check if it is a file, not a directory
        if os.path.isfile(file_path):
            # Create new filename: lowercase and replace spaces with underscores
            new_filename = filename.lower().replace(' ', '_')
            
            # Construct full new file path
            new_file_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

# Example usage: specify the folder path you want to process
rename_files_in_folder(csv_destination_folder)
