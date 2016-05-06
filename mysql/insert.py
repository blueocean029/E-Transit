import MySQLdb

db = MySQLdb.connect("localhost","root","0000","mydb" )

cursor = db.cursor()

f1=raw_input("Enter the first name of the Employee : ")
f2=raw_input("Enter the last name of the Employee : ")
f3=raw_input("Enter the age of the Employee : ")
f4=raw_input("Enter the sex of the Employee(M\F) : ")
f5=raw_input("Enter the income of the Employee : ")

try:
   cursor.execute("""INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES (%s,%s,%s,%s,%s)""",(f1,f2,f3,f4,f5))
   db.commit()
except:
   db.rollback()

db.close()
