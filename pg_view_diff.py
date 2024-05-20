import psycopg2

# Подключение к первой СУБД - Постгрес #1
conn_pg1 = psycopg2.connect(
    dbname="db",
    user="postgres",
    password="pass",
    host="1.2.3.4",
    port="30161"
)
cursor_pg1 = conn_pg1.cursor()

# Подключение к второй СУБД - Постгрес #2
conn_pg2 = psycopg2.connect(
    dbname="db",
    user="postgres",
    password="pass",
    host="2.3.4.5",
    port="32027"
)
cursor_pg2 = conn_pg2.cursor()

# Инициализация словарей для хранения данных
pg_1_dict = {}
pg_2_dict = {}
pg_3_dict = {}

# Получение списка всех view в схеме dm_udh_csk_zapolyarye на первом сервере
cursor_pg1.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'dm_udh_csk_zapolyarye' AND table_type = 'VIEW';")
views_pg1 = cursor_pg1.fetchall()

# Получение count записей для каждого view на первом сервере
for view in views_pg1:
    cursor_pg1.execute(f"SELECT COUNT(*) FROM dm_udh_csk_zapolyarye.{view[0]};")
    count = cursor_pg1.fetchone()[0]
    pg_1_dict[view[0]] = count

# Получение списка всех view в схеме dm_udh_csk_zapolyarye на втором сервере
cursor_pg2.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'dm_udh_csk_zapolyarye' AND table_type = 'VIEW';")
views_pg2 = cursor_pg2.fetchall()

# Получение count записей для каждого view на втором сервере и сравнение с первым сервером
for view in views_pg2:
    cursor_pg2.execute(f"SELECT COUNT(*) FROM dm_udh_csk_zapolyarye.{view[0]};")
    count = cursor_pg2.fetchone()[0]
    pg_2_dict[view[0]] = count

    if view[0] in pg_1_dict and pg_1_dict[view[0]] != count:
        pg_3_dict[view[0]] = abs(pg_1_dict[view[0]] - count)

# Вывод отличающихся count записей в каждом view
print("Различия в количестве записей между серверами:")
for view, diff_count in pg_3_dict.items():
    print(f"View: {view}, Разница: {diff_count}")

print("pg_2_dict pg_2_dict pg_2_dict:::")
for view, diff_count in pg_2_dict.items():
    print(f"View: {view}, count: {diff_count}")

# Закрытие курсоров и соединений
cursor_pg1.close()
cursor_pg2.close()
conn_pg1.close()
conn_pg2.close()
