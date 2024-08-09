import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Задание: Исследование оценок учеников

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'gender': ['female', 'male', 'male', 'male', 'female', 'male', 'female', 'female', 'male', 'male'],
    'math': [85, 78, 92, 88, 76, 95, 89, 84, 91, 80],
    'science': [90, 82, 85, 87, 77, 92, 88, 90, 86, 83],
    'english': [88, 79, 95, 84, 81, 93, 87, 85, 89, 78],
    'history': [92, 76, 89, 90, 75, 88, 91, 82, 84, 77],
    'art': [87, 90, 83, 86, 80, 91, 85, 88, 94, 79]
}

df = pd.DataFrame(data)
print(df.head())

# Вычислите среднюю оценку по каждому предмету
print('\nMean math: ' + str(df['math'].mean()))
print('Mean science: ' + str(df['science'].mean()))
print('Mean english: ' + str(df['english'].mean()))
print('Mean history: ' + str(df['history'].mean()))
print('Mean art: ' + str(df['art'].mean()))

# Вычислите медианную оценку по каждому предмету
print('\nMedian math: ' + str(df['math'].median()))
print('Median science: ' + str(df['science'].median()))
print('Median english: ' + str(df['english'].median()))
print('Median history: ' + str(df['history'].median()))
print('Median art: ' + str(df['art'].median()))


# Вычислите Q1 и Q3 для оценок по математике:
Q1_math = df['math'].quantile(0.25)
Q3_math = df['math'].quantile(0.75)
IQR_math = Q3_math - Q1_math

downside = Q1_math - 1.5 * IQR_math
upside = Q3_math + 1.5 * IQR_math

df_new = df[(df['math'] >= downside) & (df['math'] <= upside)]

df_new.boxplot(column='math')
plt.show()

# Вычислите стандартное отклонение
print('\nStd math: ' + str(df['math'].std()))
print('Std science: ' + str(df['science'].std()))
print('Std english: ' + str(df['english'].std()))
print('Std history: ' + str(df['history'].std()))
print('Std art: ' + str(df['art'].std()))