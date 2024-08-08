import pandas as pd

df = pd.read_csv('games_dataset.csv')

print(df.head(5))

print(df.info())

print(df.describe())


df = pd.read_csv('dz.csv')

print(df)

df.dropna( inplace=True)

print(df)

group = df.groupby('City')['Salary'].mean()

print(group)
