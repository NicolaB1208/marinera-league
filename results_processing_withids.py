import csv
import os

# SQL commands to export the couples table to a csv
#.headers on
#.mode csv
#.output database_export/couples.csv
#SELECT * FROM couples;
#.output stdout

# Categories list
input_folder = "source-files/2024/cl-madrid/ai-results/eliminatoria/single"
output_file = 'source-files/2024/cl-madrid/ai-results/combined_eliminatoria_single.csv'
final_header = ['category','name','couple_number','judge_1','judge_2','judge_3','judge_4','judge_5','total_score','qualified']  # Add your desired columns here

def combine_csv_files(input_folder, output_file, final_header):
    # Create the output CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=final_header)
        writer.writeheader()  # Write the header row
        
        # Iterate through all files in the folder
        for filename in os.listdir(input_folder):
            if filename.endswith('.csv') and filename != output_file:
                file_path = os.path.join(input_folder, filename)  # Full path to the file
                
                # Read each CSV file
                with open(file_path, 'r', encoding='utf-8') as infile:
                    reader = csv.reader(infile)  # Using csv.reader to ignore headers
                    next(reader)  # Skip the header row in the input files
                    
                    for row in reader:
                        # Align the row to the final_header order
                        new_row = {
                            'category': filename.replace('ai_processed_', '').replace('.csv', ''),  # Extract category from filename
                            'name': row[0],       # Assuming 'names' is the first column in the input files
                            'couple_number': row[1],  # Assuming 'couple_number' is the second column
                            'judge_1': row[2],     # Assuming the judges' scores follow
                            'judge_2': row[3],
                            'judge_3': row[4],
                            'judge_4': row[5],
                            'judge_5': row[6],
                            'total_score': row[7],  # Assuming 'total_score' comes after the judges
                            'qualified': row[8],   # Assuming 'qualified' is the last column
                        }
                        
                        writer.writerow(new_row)

# Call the function to combine CSV files
#combine_csv_files(input_folder, output_file, final_header)

# Step 1: Read the second CSV and create a name-to-id mapping
def create_name_id_mapping(name_id_file):
    name_to_id = {}
    with open(name_id_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name_to_id[row['name']] = row['id']
    return name_to_id

# Step 2: Read the first CSV and substitute names with IDs
def substitute_names_with_ids(results_file, name_to_id_mapping, output_file):
    with open(results_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = ['category','person_id','couple_number','judge_1','judge_2','judge_3','judge_4','judge_5','total_score','qualified']  # Get the original fieldnames

        # Create a new CSV file to write the results
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row

            for row in reader:
                # Replace couple_name_1 and couple_name_2 with their corresponding ids
                row['person_id'] = name_to_id_mapping.get(row['name'], row['name'])  # Keep name if no id is found
                

                writer.writerow({
                    'category': row['category'],
                    'person_id': row['person_id'],  # Use the new column names for the output
                    'couple_number': row['couple_number'],
                    'judge_1': row['judge_1'],
                    'judge_2': row['judge_2'],
                    'judge_3': row['judge_3'],
                    'judge_4': row['judge_4'],
                    'judge_5': row['judge_5'],
                    'total_score': row['total_score'],
                    'qualified': row['qualified'],
                })

# File paths
name_id_file = 'source-files/2024/cl-madrid/database_export/people.csv'  # CSV with id and names columns
results_file = output_file  # CSV with couple_name_1 and couple_name_2
output_file = 'source-files/2024/cl-madrid/ai-results/combined_eliminatoria_withids_single.csv'  # Output file to save the result

# Step 3: Perform the substitution
name_to_id_mapping = create_name_id_mapping(name_id_file)
substitute_names_with_ids(results_file, name_to_id_mapping, output_file)

print("Substitution completed and saved to:", output_file)
