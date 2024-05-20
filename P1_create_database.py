import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="")

cur = conn.cursor()

sql="CREATE DATABASE Library"

cur.execute(sql)

print("Database Created Successfully")

cur.close()
conn.close()