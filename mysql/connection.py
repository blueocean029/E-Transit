import MySQLdb

db = MySQLdb.connect("localhost","root","0000","mydb" )

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print "Database version : %s " % data


