import mysql.connector
def db_conn_func():
    return mysql.connector.connect(
    host='localhost',
    user='root',
    password='***********', 
    database='pdbc'
)

