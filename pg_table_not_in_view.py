import psycopg2

# Подключение к БД PostgreSQL
conn = psycopg2.connect(
    dbname="db",
    user="postgres",
    password="pass",
    host="1.2.3.4",
    port="32027"
)
cursor = conn.cursor()

# Получение списка всех таблиц в схеме dm_udh_csk_zapolyarye
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'dm_udh_csk_zapolyarye' AND table_type = 'BASE TABLE';")
all_tables = [table[0] for table in cursor.fetchall()]

# Получение списка всех view в схеме dm_udh_csk_zapolyarye
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'dm_udh_csk_zapolyarye' AND table_type = 'VIEW';")
views = [view[0] for view in cursor.fetchall()]

unused_tables = all_tables.copy()

# Проверка источников данных для каждого представления
for view in views:
    cursor.execute(f"SELECT table_name FROM information_schema.view_table_usage WHERE table_schema = 'dm_udh_csk_zapolyarye' AND view_name = '{view}';")
    source_tables = [table[0] for table in cursor.fetchall()]
    for source_table in source_tables:
        if source_table in unused_tables:
            unused_tables.remove(source_table)

# Вывод списка таблиц, которые не используются в представлениях
print("Таблицы, которые не используются в представлениях:")
for table in unused_tables:
    print(table)

# Закрытие курсора и соединения
cursor.close()
conn.close()