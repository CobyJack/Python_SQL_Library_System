import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="", database="library")

cur = conn.cursor()

#Fetch Readers and Create Rented books Table
c_id=int(input("Enter Card ID: "))
rsql="SELECT name, cbr FROM readers WHERE cid="+str(c_id)+" "
cur.execute(rsql)
result=cur.fetchone()
print("ID\t\t\t   Name\t   Rented Books")
print(c_id,"\t\t  ",result[0],"\t",result[1])


#Fetch and Rent Books
bsql="SELECT bname from books"
cur.execute(bsql)

books=cur.fetchall()
bl=[]
c=1
print("Welcome to Infinity Library.\nWhich of the following books would you like to rent")
print("Id\tName")
for name in books:
    print(c,"\t",name[0],sep="")
    bl.append(name[0])
    c+=1

rid=int(input("Enter the Id of the book you want to rent: "))

confirm_rent=input("Do you want to rent the book: "+bl[rid-1]+"? (y/n)")
# bname=bl[rid]
if (confirm_rent=='y'):

    c=1 #Misc Variable
    flag=1
    bsql="SELECT isbn, bname, qty, rented FROM books WHERE id="+str(rid)+" "
    cur.execute(bsql)

    # t=cur.fetchone()
    # print(t)

    isbn, bname, qty, rent_count=cur.fetchone()
    qty-=1
    rent_count+=1

    print()
    bsql="UPDATE books SET qty=%s, rented=%s WHERE id=%s"
    val=(qty,rent_count,rid)
    cur.execute(bsql,val)
    conn.commit()
    print(cur.rowcount,"row(s) affected in Books Table")


    rsql="SELECT name, cbr FROM readers WHERE cid="+str(c_id)+""
    cur.execute(rsql)

    print()
    user_name, cur_books_rent=cur.fetchone()
    cur_books_rent+=1
    print(user_name,"rented",cur_books_rent,"book(s)")
    print("Current book rented:",bname)

    print()
    rsql="UPDATE readers SET cbr=%s WHERE cid=%s"
    val=(cur_books_rent,c_id)
    cur.execute(rsql,val)
    conn.commit()
    print(cur.rowcount,"row(s) affected in Readers Table")

    usql="SELECT rent_count, isbn FROM reader_"+user_name+"_rented WHERE isbn="+str(isbn)+" "
    # val=(user_name, isbn)
    cur.execute(usql)
    
    try:
        rented_count, usr_isbn= cur.fetchone()
    except TypeError:
        flag=0
        rented_count=c
        usr_isbn=isbn
        pass
    
    if flag==0:
        usql="INSERT INTO reader_"+user_name+"_rented(cid, bname, isbn, rent_count) VALUES (%s,%s,%s,%s)"
        val=(c_id, bl[rid-1], isbn, rented_count)
        cur.execute(usql,val)
        conn.commit()
        print(cur.rowcount,"row(s) affected in",user_name,"Rented Table")
    else:
        # usql="SELECT rented FROM "+user_name+"_rented WHERE isbn="+str(isbn)+" "
        # val=(user_name,isbn)
        rented_count+=1
        usql="UPDATE reader_"+user_name+"_rented SET rent_count="+str(rented_count)+" WHERE isbn="+str(isbn)+" "
        cur.execute(usql)
        conn.commit()
        print(cur.rowcount,"row(s) affected in",user_name,"Rented Table")

else:
    print("You are free to explore the library as you please")

