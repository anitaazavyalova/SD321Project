import pandas as pd

df = pd.read_csv("us_college_earnings.csv")

#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())
#Regarding the data, we agreed to completely get rid of SAT_Average because in the overarching question something that is only a factor of getting into a college won't necessarily impact someone's future socioeconomic status
#We also agreed to take away Lat and Longtitude because if anything we can always search up their location rather than using specific coordinates.

#We agreed that we shouldn't need to add any new variables because at a certain point when computing various statistics needed to complete our analysis, too many variables won't really be adding much.
df_clean  = df.dropna(subset = ['admission_rate'])  
df_filled = df.fillna('unknown')      # fill: replace every missing value with value
print(len(df) - len(df.dropna()))

print(df_filled.head())
