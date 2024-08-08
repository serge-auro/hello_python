import pandas as pd

# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# print(series)

df = pd.read_csv('World-happiness-report-2024.csv')
print(df[df['Healthy life expectancy'] > 0.7])
