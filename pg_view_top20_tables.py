import psycopg2
import csv

# Подключение к PostgreSQL
conn = psycopg2.connect(
    host="1.2.3.4",
    port="5432",
    database="pg1",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

# Получение списка текущих таблиц
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
tables = cursor.fetchall()

data = []

# Получение статистики для каждой таблицы
for table in tables:
    table_name = table[0]

    # Получение количества строк в таблице
    cursor.execute(f'SELECT count(*) FROM public."{table_name}"')
    row_count = cursor.fetchone()[0]

    # Получение объема таблицы в Гб
    print(f"SELECT pg_size_pretty(pg_total_relation_size('public.\"{table_name}\"'))")
    cursor.execute(f"SELECT pg_size_pretty(pg_total_relation_size('public.\"{table_name}\"'))")
    table_size = cursor.fetchone()[0]

    data.append((table_name, table_size, row_count))

# Сортировка по количеству строк и вывод ТОП-20 в csv
data.sort(key=lambda x: x[2], reverse=True)
top_20 = data[:20]

# Запись данных в csv файл
with open('table_statistics.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Имя таблицы', 'Количество ГБ', 'Количество строк'])
    writer.writerows(top_20)

# Закрытие соединения
cursor.close()
conn.close()
