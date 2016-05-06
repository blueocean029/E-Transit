import MySQLdb


db = MySQLdb.connect("localhost","root","0000","mydb" )

cursor = db.cursor()

name = raw_input("Enter the First Name of the employee : ")

try:

   cursor.execute("DELETE FROM EMPLOYEE WHERE FIRST_NAME = %s",name)
   
   db.commit()
except:
   db.rollback()

db.close()
