import pandas as pd

df = pd.read_csv('games_dataset.csv')



print(df.info())

print(df.describe())


df = pd.read_csv('dz.csv')

group = df.groupby('City')['Salary'].mean()

print("\n group by city - avg Salary: \n")

print(group)
