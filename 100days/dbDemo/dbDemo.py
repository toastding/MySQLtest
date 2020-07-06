import pymysql

db = pymysql.connect("localhost", "root", "0000", "test_db")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s" % data)
db.close()

