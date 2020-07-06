import pymysql

db = pymysql.connect("localhost", "root", "0000", "test_db")
cursor = db.cursor()
sql = """INSERT INTO EMPLOYEE(
         FIRST_NAME,LAST_NAME,AGE,SEX,
         INCOME)
         VALUES ("Bob", "Ting", 25, 'F', 3000),
                ("Rick", "Hyper", 22, 'M', 6000)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
