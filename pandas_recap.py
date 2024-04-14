import pandas as pd


file_path = "example.csv"


# Read data from a CSV file into a DataFrame
df = pd.read_csv(file_path)


# Display the first few rows of the DataFrame
print("\nFirst few rows of the DataFrame:")
print(df.head())


# Display basic information about the DataFrame
print("\nBasic information about the DataFrame:")
print(df.info())


# Perform descriptive statistics on numerical columns of the DataFrame
print("\nDescriptive statistics for numerical columns:")
print(df.describe())


# Perform descriptive statistics on categorical columns of the DataFrame
print("\nDescriptive statistics for categorical columns:")
print(df.describe(include='object'))


# Select specific columns from the DataFrame
columns = ['Kategorie1', 'Kategorie2']
selected_df = df[columns]
print("\nSelected columns:")
print(selected_df)


# Filter rows based on a condition
condition = 'Kategorie1 < 20'
filtered_df = df[df.eval(condition)]
print("\nFiltered DataFrame:")
print(filtered_df)


# Export DataFrame to a CSV file
filtered_df.to_csv("output.csv", index=False)
print("\nDataFrame exported successfully to: output.csv")


