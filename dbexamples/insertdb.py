# connect to postgresql database
# pip install psycopg2
import sys
import psycopg2 # cx_Oracle

bookid = int(input("Enter book id"))
booktitle = input("Enter book title")

conn = psycopg2.connect(host='localhost',user='demodbuser_1',password='password',dbname='demodb_1')

if not conn:
    sys.exit()

cur = conn.cursor()

try:
    #cur.execute("insert into books values(1,'programming in c')")
    cur.execute("insert into books values({},'{}')".format(bookid, booktitle))
    conn.commit()
except Exception as e:
    print(e)
else:
    print("record created")
finally:
    conn.close()
