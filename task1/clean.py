import pandas as pd

df = pd.read_csv('SPX.csv')

print("--- 1. First 5 rows of the dataset ---")
print(df.head())

print("\n--- 2. Dataset Information ---")
print(df.info())

print("\n--- 3. Checking for Missing Values ---")
print(df.isnull().sum())

print("\n--- 4. Checking for Duplicate Rows ---")
print("Number of duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()
df = df.dropna()

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

print("\n--- 5. Data Cleaning Completed Successfully! ---")
print("Cleaned Dataset Shape:", df.shape)

df.to_csv('cleaned_SPX.csv', index=False)
print("Cleaned file saved as 'cleaned_SPX.csv'")
