import MySQLdb
import sys
import getpass

db = MySQLdb.connect("localhost","root","0000","mydb" )

cursor = db.cursor()
user = raw_input("Username : ")
password = raw_input("Password : ")
#password=getpass.getpass()

if user == "" :
    print "Username or password missing!"
    print "Login Again."
    sys.exit()
elif password == "":
     print "Username or password missing!"
     print "Login Again."
     sys.exit()

try:

   cursor.execute("SELECT * FROM login \
       WHERE username = %s",user)
   data = cursor.fetchall()
   
   if len(data) == 0:
        print "Invalid username or password!"
        sys.exit()
   else:
        print "Seccussfully login!"
   
except:
   print "Error: unable to fecth data"

db.close()
