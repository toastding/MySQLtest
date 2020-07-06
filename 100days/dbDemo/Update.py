import pymysql

db = pymysql.connect("localhost", "root", "0000", "test_db")
cursor = db.cursor()

sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()


