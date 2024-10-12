import csv

# SQL commands to export the people table to a csv
#.headers on
#.mode csv
#.output people.csv
#SELECT * FROM people;
#.output stdout

# List of file paths you want to process
files_paths = ['ai_processed_adulto.csv', 'ai_processed_single_a.csv']  # Replace with actual file paths

# Create the output CSV file once and write the header
with open('people_separated.csv', 'w', newline='') as output_file:
    fieldnames = ['name']  # Specify the fieldnames
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write the header once before processing files
    
    # Loop through each file in the list
    for file_path in files_paths:
        # Open each file
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)  # Use DictReader to read the CSV into a dictionary
            
            # Process each row in the file
            for row in reader:
                names = row['names']  # Access the 'names' column directly by key
                if ' y ' in names:
                    first_name, second_name = names.split(' y ')
                    writer.writerow({
                        'name': first_name.strip()                        
                    })
                    writer.writerow({
                        'name': second_name.strip()
                    })
                else:
                    writer.writerow({
                        'name': names.strip()
                    })
