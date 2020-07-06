import pymysql

db = pymysql.connect("localhost", "root", "0000", "test_db")
cursor = db.cursor()
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s " % 1000
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income))

except:
    print("Error : unable to fecth data")

db.close()
