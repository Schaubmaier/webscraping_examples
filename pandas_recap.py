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


# Create dataframe
data_list = [["A", 10], ["B", 20], ["C", 30], ["D", 40]]
df = pd.DataFrame(data_list, columns=['Col1', 'Col2'])
print("\nDataframe:")
print(df.head())

data_dict = {'Col1': [1, 2, 5], 'Col2': [3, 4, 7]}
df = pd.DataFrame(data_dict)
print("\nDataframe:")
print(df.head())



# Export DataFrame to a CSV file
df.to_csv("output.csv", index=False)
print("\nDataFrame exported successfully to: output.csv")


