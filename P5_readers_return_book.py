import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="library")

cur = conn.cursor()

#Fetch User Data
print("Log in to your account to return the book(s)")

c_id=int(input("Enter your Card ID: "))
user_name=input("Enter your name: ")

rsql = "SELECT cbr FROM readers WHERE cid="+str(c_id)+" "
cur.execute(rsql)

try:
    cur_rent_count_tuple = cur.fetchone()
    cur_rent_count=cur_rent_count_tuple[0]
except TypeError:
    cur_rent_count=0


if cur_rent_count!=0:


    # Fetch Book Data
    bl=[]
    bsql = "SELECT bname FROM books"
    cur.execute(bsql)
    books = cur.fetchall()
    for info in books:
        bl.append(info[0])

    c=1 # Counter to print Book ID NOT ISBN
    print("ID\tBook Name")
    for info in bl:
        print(c,"\t",info, sep="")
        c+=1

    rid = int(input("Enter the ID of the Book which you want to return: "))

    bsql = "SELECT isbn, qty, rented FROM books WHERE id="+str(rid)+" "
    cur.execute(bsql)
    isbn, qty, rented = cur.fetchone()

    usr_sql="SELECT bname, rent_count from reader_"+user_name+"_rented WHERE isbn="+str(isbn)+" "
    # val=(isbn)
    cur.execute(usr_sql)
    try:
        bname, rent_count = cur.fetchone()
    except TypeError:
        bname=""
        rent_count=0
        print("You can't return this book as you have not rented it yet!")
        conn.close()
    else:
        confirm_return = input("Do you really want to return this book? (y/n): ")
        if (confirm_return=='y' and rent_count>=2):
            rent_count-=1
            usr_sql = "UPDATE reader_"+user_name+"_rented SET rent_count=%s WHERE  isbn=%s"
            val=(rent_count, isbn)
            cur.execute(usr_sql,val)
            conn.commit()
            print(cur.rowcount,"row(s) affected in reader_"+user_name+"_rented")

            cur_rent_count-=1
            rsql = "UPDATE readers SET cbr=%s WHERE cid=%s"
            val=(cur_rent_count, c_id)
            cur.execute(rsql,val)
            conn.commit()
            print(cur.rowcount,"row(s) affected in Readers Table\n")

            qty+=1
            rented-=1
            bsql="UPDATE books SET qty=%s, rented=%s WHERE isbn=%s"
            val=(qty, rented, isbn)
            cur.execute(bsql, val)
            conn.commit()
            print(cur.rowcount,"row(s) affected in Books Table\n")
        
        elif (confirm_return=='y' and rent_count==1):
            usr_sql = "DELETE FROM reader_"+user_name+"_rented WHERE isbn="+str(isbn)+" "
            # val=(isbn)
            cur.execute(usr_sql)
            conn.commit()
            print(cur.rowcount,"row(s) affected in reader_"+user_name+"_rented Table\n")
            
            cur_rent_count-=1
            rsql = "UPDATE readers SET cbr=%s WHERE cid=%s"
            val=(cur_rent_count, c_id)
            cur.execute(rsql, val)
            conn.commit()
            print(cur.rowcount,"row(s) affected in Readers Table\n")

            qty+=1
            rented-=1
            bsql="UPDATE books SET qty=%s, rented=%s WHERE isbn=%s"
            val=(qty, rented, isbn)
            cur.execute(bsql, val)
            conn.commit()
            print(cur.rowcount,"row(s) affected in Books Table\n")

        else:
            print("You are free to explore the library as you please")
            conn.close()