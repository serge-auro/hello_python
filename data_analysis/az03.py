import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=30, color='blue', edgecolor='black')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.show()


# Генерация двух наборов случайных данных
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.scatter(x, y, color='red')
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
