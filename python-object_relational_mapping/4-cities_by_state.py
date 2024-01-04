import MySQLdb
from sys import argv
mysql_username = argv[1]
mysql_password = argv[2]
mysql_database = argv[3]
dbconnect = MySQLdb.connect(host='localhost', port=3306, user=mysql_username, password=mysql_password, db=mysql_database)
cursor = dbconnect.cursor()
cursor.execute("SELECT cities.id, cities.name , states.name FROM cities INNER JOIN states ON states.id = cities.state_id")
cities = cursor.fetchall()
for city in cities:
    print(city)
# Close all cursors
cursor.close()
# Close all databases
dbconnect.close()