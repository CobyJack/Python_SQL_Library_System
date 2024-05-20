import mysql.connector, random

conn = mysql.connector.connect(host="localhost",user="root",password="", database="library")

cur = conn.cursor()

# Insert Librarian Data
# asql="INSERT INTO librarian(uname, exp, pin) VALUES (%s,%s,%s)"
# for _ in range(3):
#     n=input("Enter username: ")
#     xp=int(input("Enter your Experience: "))
#     pin=int(input("Enter your pin: "))
#     val=(n,xp,pin)
#     cur.execute(asql,val)
#     conn.commit()
#     print(cur.rowcount,"row(s) affected in Librarian Table")

# Insert Reader Data
rsql="INSERT INTO readers(cid, name, cbr) VALUES (%s,%s,%s)"
for _ in range(2):
    id_gen=random.randint(10000000,999999999)
    n=input("Enter username: ")
    cbr=0
    val=(id_gen,n,cbr)  
    cur.execute(rsql,val)
    conn.commit()
    print(cur.rowcount,"row(s) affected in Readers Table")
    
    usr_sql="CREATE TABLE reader_"+n.lower()+"_rented (cid BIGINT, bname varchar (50), isbn BIGINT, rent_count int(4))"
    cur.execute(usr_sql)
    print(f"reader_{n}_rented Table created")

# Insert Book Data
# bsql="INSERT INTO books(isbn, bname, qty, rented) VALUES (%s,%s,%s,%s)"
# for _ in range(2):
#     isbn_gen=random.randint(1000000000,9999999999)
#     bn=input("Enter Book Name: ")
#     qty=int((random.random())*100)
#     rented=0
#     val=(isbn_gen,bn,qty,rented)
#     cur.execute(bsql,val)
#     conn.commit()
#     print(cur.rowcount,"row(s) affected in Books Table")

cur.close()
conn.close()