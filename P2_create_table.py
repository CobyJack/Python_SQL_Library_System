import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="", database="library")

cur = conn.cursor()

# sql="CREATE TABLE librarian(id integer AUTO_INCREMENT PRIMARY KEY, uname varchar(30) UNIQUE, exp int(4), pin BIGINT)"
# cur.execute(sql)
# print("Librarian Table Created Successfully")

# sql = "CREATE TABLE readers(cid BIGINT UNIQUE, name varchar(30), cbr int(4))"
# cur.execute(sql)
# print("Readers Table Created Successfully")

sql = "CREATE TABLE books(isbn BIGINT UNIQUE, bname varchar(90), qty int(4), rented int(4))"
cur.execute(sql)
print("Books Table Created Successfully")

cur.close()
conn.close()