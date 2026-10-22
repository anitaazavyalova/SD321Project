import pandas as pd

df = pd.read_csv("us_college_earnings.csv")

#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())
#Regarding the data, we agreed to completely get rid of SAT_Average because in the overarching question something that is only a factor of getting into a college won't necessarily impact someone's future socioeconomic status
#We also agreed to take away Lat and Longtitude because if anything we can always search up their location rather than using specific coordinates.


cols_to_drop = ['sat_average', 'latitude', 'longitude']
df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])
df_clean = df.dropna(subset=['admission_rate']).copy()

categorical_cols = ['city', 'state', 'region', 'control', 'level', 'predominant_degree']
for col in categorical_cols:
    if col in df_clean.columns:
        df_clean[col] = df_clean[col].fillna('Unknown')

print(df_clean.head())
print(df_clean.info())

