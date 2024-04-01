import pandas as pd

# ingest data 
url = "proj1_datafile.csv"
df = pd.read_csv(url)

# Display column names of the DataFrame
print("Column Names:")
print(df.columns)

# display 10 rows of the dataFrame 
print("\nOriginal Data:")
print(df.head(10))

# Clean the data to handle missing values/outliers

df.dropna(inplace=True)  # Remove rows with missing values

#  Outliers (ex: delete rows where the value in the 'value' column is > 1000)

df['Name'] = pd.to_numeric(df['Name'], errors='coerce')  # Convert 'Name' column to numeric, coerce errors to NaN

# filter out rows with 'Name' > than 1000
df = df[df['Name'] <= 1000]

# show the cleaned DataFrame
print("\nCleaned Data:")
print(df.head())
