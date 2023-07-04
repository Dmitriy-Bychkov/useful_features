# Version 1
import psycopg2
import csv

"""Скрипт для заполнения данными таблиц в БД Postgres."""
with open('./north_data/employees_data.csv') as f:
    emp_data = []
    data = csv.reader(f, delimiter=",")
    for line in data:
        n = tuple(line)
        emp_data.append(n)

with open('./north_data/customers_data.csv') as f:
    cust_data = []
    data = csv.reader(f, delimiter=",")
    for line in data:
        n = tuple(line)
        cust_data.append(n)

with open('./north_data/orders_data.csv') as f:
    ord_data = []
    data = csv.reader(f, delimiter=",")
    for line in data:
        n = tuple(line)
        ord_data.append(n)

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='320670')
cur = conn.cursor()
cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', emp_data)
cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', cust_data)
cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', ord_data)
conn.commit()

cur.close()
conn.close()

#################################################################
# Version 2
"""Скрипт для заполнения данными таблиц в БД Postgres."""
# from utils.csv_reader import *
# from utils.db_connector import db_connector
from csv_files_reader import csv_reader
from postgres_db_connector import db_connector

# Пути к файлам CSV для удобства записаны в переменные
employees_filename = 'north_data/employees_data.csv'
customers_filename = 'north_data/customers_data.csv'
orders_filename = 'north_data/orders_data.csv'

# Списки с данными из файлов CSV записываются в переменные
employees_data = csv_reader(employees_filename)
customers_data = csv_reader(customers_filename)
orders_data = csv_reader(orders_filename)

# Подключение к базе данных PostgreSQL
db_conn = db_connector()

# Блок добавления в базу данных потаблично
try:
    with db_conn:
        with db_conn.cursor() as cur:
            for row in customers_data:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                            (row['customer_id'], row['company_name'], row['contact_name']))
            for row in employees_data:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                            (row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date'],
                             row['notes']))
            for row in orders_data:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                            (row['order_id'], row['customer_id'], row['employee_id'], row['order_date'],
                             row['ship_city']))
finally:
    db_conn.close()
