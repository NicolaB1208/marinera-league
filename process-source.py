import pandas as pd

# Load the Excel file
excel_file = 'source-files/2024/cl-madrid/cl-madrid-2024-eliminatoria-original.xlsx'

# Load all the sheets into a dictionary of DataFrames
all_sheets = pd.read_excel(excel_file, sheet_name=None)

# Loop through each sheet and save as a separate CSV
for sheet_name, df in all_sheets.items():
    # Save each sheet to a CSV file
    df.to_csv(f'source-files/2024/cl-madrid/eliminatoria/{sheet_name}.csv', index=False)
