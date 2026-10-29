'''
lab09
m281134, c. l. chau
m287116, a. a. zavyalova
m282418, o. k. green
'''

import pandas as pd

print('1.')

#we are pulling the columns we think we''ll use
cols = ['UNITID', 'INSTNM', 'STABBR', 'CONTROL', 'ICLEVEL']
df = pd.read_csv('./csv/hd2025.csv', usecols=cols)

print(df.head())
df.info()
print(df.describe())
print(df.isnull().sum())

print('2.')
df = df[cols]
df.columns = ['unitid', 'institution', 'state', 'control', 'level']

for col in ['institution', 'state']:
    df[col] = df[col].str.strip()

df['state'] = df['state'].str.upper()
for col in ['unitid', 'control', 'level']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print('3.')
df = df.dropna(subset=['unitid', 'institution', 'state'])
df = df.drop_duplicates(subset=['unitid'])


print('valid institutions:', len(df))
df.to_csv('./cleaned/team4_institutions.csv', index=False)
