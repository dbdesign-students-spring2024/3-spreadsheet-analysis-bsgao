# place your code to clean up the data file below.
import pandas as pd

df = pd.read_csv("/Users/brandongao/spreadsheet/data/2019_DOE_High_School_Directory_20240219.csv")
numerical_df = df.select_dtypes(include=['number'])
numerical_df = pd.concat([df[['school_name']], numerical_df], axis=1)

# dropping the columns with less than 200 non- N/A values
columns_to_drop = [col for col in numerical_df.columns[1:] if numerical_df[col].dropna().shape[0] < 200]
df = numerical_df.drop(columns=columns_to_drop)

#dropping the columns with values that are not in the range of 0 to 1
columns_to_drop = [col for col in df.columns[1:] for j in df[col] if j > 1 or j< 0]
df = df.drop(columns=columns_to_drop)

# Filled the missing values with the average of the column since there is not many missing values for the cleaned data
mean = df.mean().round(2)
df = df.fillna(mean)

# Exporting the csv to the data folder
df.to_csv('/Users/brandongao/spreadsheet/data/cleaned_data.csv', index=False)


