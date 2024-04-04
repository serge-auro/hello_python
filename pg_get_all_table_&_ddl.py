import psycopg2
import csv

DB_NAME = "postgres"
USER = "postgres"
PASS = "postgres"
HOST = "1.2.3.4"
PORT = "32027"
count = 0
conn = None
cur = None

def new_connection(db_name):
    global conn, cur
    conn = psycopg2.connect(
        dbname=db_name,
        user=USER,
        password=PASS,
        host=HOST,
        port=PORT
    )
    cur = conn.cursor()

# Функция для получения данных из таблицы и сохранения их в CSV
def extract_data_and_save(database, table):
    global count
    cur.execute(f"SELECT * FROM {table} LIMIT 100")
    rows = cur.fetchall()
    print(f"Writing data from {database}.{table} into CSV...")

    with open(f"{database}.{table}.csv", "w", newline="", encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, escapechar='\\')
        csvwriter.writerow([desc[0] for desc in cur.description])
        csvwriter.writerows(rows)
    count += 1
    generate_ddl(cur, database, table)

# Функция для генерации и сохранения DDL для таблицы
def generate_ddl(cur, database, table):
    cur.execute(f"SELECT 'CREATE TABLE ' || table_name || ' (' || string_agg(column_name || ' ' || data_type, ', ') || ')' AS ddl FROM information_schema.columns WHERE table_name = '{table}' GROUP BY table_name, table_schema")
    ddls = cur.fetchall()
    print(f"ddl= {ddls}")

    with open(f"{database}.{table}.sql", "w", newline="", encoding="utf-8") as csvfile:
        for ddl in ddls:
            csvfile.write(ddl[0] + "\n")


# MAIN
# Получение списка всех баз данных
new_connection(DB_NAME)
cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false AND datname != 'postgres'")
databases = [database[0] for database in cur.fetchall()]
cur.close()
conn.close()
# Проход по всем базам данных, схемам public и таблицам
for database in databases:
    new_connection(database)
    print(f"database= {database}")
    cur.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    tables = [table[0] for table in cur.fetchall()]
    for table in tables:
        extract_data_and_save(database, f"{table}")
    cur.close()
    conn.close()

print(f"The Data of {count} tables have been written into CSV files")

# Закрытие соединения
cur.close()
conn.close()
