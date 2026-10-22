import pandas as pd

df = pd.read_csv("us_college_earnings.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())