# connect to postgresql database
# pip install psycopg2
import sys
import psycopg2 # cx_Oracle

conn = psycopg2.connect(host='localhost',user='demodbuser_1',password='password',dbname='demodb_1')

if not conn:
    sys.exit()

cur = conn.cursor()

try:
    cur.execute("select * from books")
except Exception as e:
    print(e)
else:
    records = cur.fetchall() # cur.fetchone()
    for row in records:
        print(f"ID:{row[0]},Title:{row[1]}")
finally:
    conn.close()
