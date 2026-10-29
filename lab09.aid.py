'''
lab09
m281134, c. l. chau
m287116, a. a. zavyalova
m282418, o. k. green
'''

import pandas as pd

print('1.')

#we are pulling the columns we think we''ll use
cols = ['UNITID', 'PGRNT_P', 'PGRNT_A', 'LOAN_P', 'LOAN_A']
df = pd.read_csv('./csv/sfa2324.csv', usecols=cols)

print(df.head())
df.info()
print(df.describe())
print(df.isnull().sum())

print('2.')
df.columns = df.columns.str.lower()
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print('3.')
# ipeds percent columns use a 0-100 scale
for col in ['pgrnt_p', 'loan_p']:
    df.loc[df[col] < 0, col] = None
    df.loc[df[col] > 100, col] = None

# amounts should not be negative
for col in ['pgrnt_a', 'loan_a']:
    df.loc[df[col] < 0, col] = None

df = df.dropna(subset=['unitid'])
df = df.drop_duplicates(subset=['unitid'])

print('valid aid records:', len(df))
df.to_csv('./cleaned/team4_aid.csv', index=False)
