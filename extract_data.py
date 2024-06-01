import pandas as pd

# Load the Excel file
excel_file = '2023_Energy and Emissions Roadmap_Working.xlsx'
sheet_name = '1M-NR'  # Adjust this if the sheet name is different

# Load the sheet into a DataFrame
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Extract the data you need
# Adjust the column names and indices based on your actual Excel file structure
labels = df['Year'].tolist()
annual_electricity_consumption = df['Annual Electricity Consumption (MWh)'].tolist()

# Save the extracted data to a JSON file
data = {
    'labels': labels,
    'annual_electricity_consumption': annual_electricity_consumption
}

with open('data.json', 'w') as f:
    json.dump(data, f)

print('Data extraction complete. Data saved to data.json')

