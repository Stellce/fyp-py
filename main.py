import pandas as pd

# Load the Excel file
file_path = 'your_file.xlsx'
data = pd.read_excel(file_path)

# Inspect the data
print(data.head())
