import MySQLdb

db = MySQLdb.connect("localhost","root","0000","mydb" )

cursor = db.cursor()

name = raw_input("Enter the First name of the Employee:")
temp = raw_input("Enter the update you want to do:  ")
value = raw_input("It's new value: ")

try:
   cursor.execute("UPDATE EMPLOYEE SET %s = %s WHERE FIRST_NAME = %s",(temp,value,name))

   db.commit()
except:

   db.rollback()

db.close()
