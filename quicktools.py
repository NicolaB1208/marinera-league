

# Path to your CSV file
csv_file_path = 'source-files/2024/cl-madrid/ai-results/eliminatoria/ai_processed_adulto.csv'

# Get the entire CSV content as a string
csv_content = read_csv_as_string(csv_file_path)

csv_content = f"```\n{csv_content}\n```"

print(csv_content)