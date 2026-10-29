'''
lab09
m281134, c. l. chau
m287116, a. a. zavyalova
m282418, o. k. green
'''

import pandas as pd

print('1.')

#we are pulling the columns we think we''ll use
cols = ['UNITID', 'COSTT4_A', 'C150_4', 'C150_L4', 'FIRST_GEN', 'FAMINC', 'GRAD_DEBT_MDN', 'MD_EARN_WNE_P10']
df = pd.read_csv('./csv/Most-Recent-Cohorts-Institution.csv', usecols=cols)

print(df.head())
df.info()
print(df.describe())
print(df.isnull().sum())

print('2.')
df.columns = df.columns.str.lower()

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print('3.')
# rates are stored as proportions from 0 to 1
for col in ['c150_4', 'c150_l4', 'first_gen']:
    df.loc[df[col] < 0, col] = None
    df.loc[df[col] > 1, col] = None

# costs, debt and earnings should not be negative
for col in ['costt4_a', 'faminc', 'grad_debt_mdn', 'md_earn_wne_p10']:
    df.loc[df[col] < 0, col] = None

df = df.dropna(subset=['unitid'])
df = df.drop_duplicates(subset=['unitid'])

print('valid outcome records:', len(df))
df.to_csv('./cleaned/team4_outcomes.csv', index=False)
