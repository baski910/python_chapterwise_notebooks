# connect to postgresql database
# pip install psycopg2
import sys
import psycopg2 # cx_Oracle

conn = psycopg2.connect(host='localhost',user='demodbuser_1',password='password',dbname='demodb_1')

if not conn:
    sys.exit()

cur = conn.cursor()

try:
    cur.execute("create table books(bookid int, booktitle varchar(50))")
    conn.commit()
except Exception as e:
    print(e)
else:
    print("table created")
finally:
    conn.close()
