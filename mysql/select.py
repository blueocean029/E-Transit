import MySQLdb

db = MySQLdb.connect("localhost","root","0000","mydb" )

cursor = db.cursor()
name = raw_input("Enter the First Name of the employee : ")

try:

   cursor.execute("SELECT * FROM EMPLOYEE \
       WHERE FIRST_NAME = %s",name )
   
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      
      print "First Name = %s,Last Name = %s,Age = %d,Sex = %s,Income = %d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"

db.close()
