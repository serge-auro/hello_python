import pandas as pd

df = pd.read_csv('animal.csv')

print(df)

df.fillna(0, inplace=True)

print(df)

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()

print(group)

group.to_csv('average_life_duration.csv', index=False)