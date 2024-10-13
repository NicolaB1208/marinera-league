import csv
import os

# SQL commands to export the people table to a csv
#.headers on
#.mode csv
#.output people.csv
#SELECT * FROM people;
#.output stdout

# List of file paths you want to process
folder_path = "source-files/2024/cl-madrid/ai-results/eliminatoria"
file_names = os.listdir(folder_path)
files_paths = [os.path.join(folder_path, file_name) for file_name in file_names]
#print(files_paths)

with open('source-files/2024/cl-madrid/couples_separated.csv', 'w', newline='') as output_file:
    fieldnames = ['names','couple_name_1','couple_name_2']  # Specify the fieldnames
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write the header once before processing files
    
    # Loop through each file in the list
    for file_path in files_paths:
        # Open each file
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read the CSV into a dictionary
            
            #print(reader.fieldnames)    

            # Process each row in the file
            for row in reader:
                names = row['names']  # Access the 'names' column directly by key
                if ' y ' in names:
                    first_name, second_name = names.split(' y ')
                    writer.writerow({
                        'names': names,
                        'couple_name_1': first_name.strip(),
                        'couple_name_2': second_name.strip() 
                    })
                else:
                    writer.writerow({
                        'names': names,
                    })

def remove_empty_rows(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header row

        # Write to the output file
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)  # Write the header to the new file

            # Iterate over the rows and check if the second and third columns have values
            for row in reader:
                if row[1] and row[2]:  # Check if both the second and third columns have values
                    writer.writerow(row)

# File paths
input_file = 'source-files/2024/cl-madrid/couples_separated.csv'   # Input CSV file
output_file = 'source-files/2024/cl-madrid/only_couples_separated.csv'  # Output CSV file to save the results

# Call the function to remove empty rows
#remove_empty_rows(input_file, output_file)

print("Rows without values in the second and third columns have been removed.")

# Step 1: Read the second CSV and create a name-to-id mapping
def create_name_id_mapping(name_id_file):
    name_to_id = {}
    with open(name_id_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name_to_id[row['name']] = row['id']
    return name_to_id

# Step 2: Read the first CSV and substitute names with IDs
def substitute_names_with_ids(couples_file, name_to_id_mapping, output_file):
    with open(couples_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = ['names','couple_id_1','couple_id_2']  # Get the original fieldnames

        # Create a new CSV file to write the results
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row

            for row in reader:
                # Replace couple_name_1 and couple_name_2 with their corresponding ids
                row['couple_name_1'] = name_to_id_mapping.get(row['couple_name_1'], row['couple_name_1'])  # Keep name if no id is found
                row['couple_name_2'] = name_to_id_mapping.get(row['couple_name_2'], row['couple_name_2'])  # Same here

                writer.writerow({
                    'names': row['names'],  # Use the new column names for the output
                    'couple_id_1': row['couple_name_1'],
                    'couple_id_2': row['couple_name_2']
                })

# File paths
name_id_file = 'source-files/2024/cl-madrid/people.csv'  # CSV with id and name columns
couples_file = 'source-files/2024/cl-madrid/only_couples_separated.csv'  # CSV with couple_name_1 and couple_name_2
output_file = 'source-files/2024/cl-madrid/couples_with_ids.csv'  # Output file to save the result

# Step 3: Perform the substitution
name_to_id_mapping = create_name_id_mapping(name_id_file)
substitute_names_with_ids(couples_file, name_to_id_mapping, output_file)

print("Substitution completed and saved to:", output_file)
