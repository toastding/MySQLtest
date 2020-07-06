import pymysql

db = pymysql.connect("localhost", "root", "0000", "test_db")
cursor = db.cursor()
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % 20
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()