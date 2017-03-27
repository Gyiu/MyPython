#!C:\Python27\python

# Import modules for CGI handling 
import cgi, cgitb, MySQLdb

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello Bor :D a</h2>"

db = MySQLdb.connect(host="192.168.1.8",    # your host, usually localhost
                     user="dev",         # your username
                     passwd="traspaC123",  # your password
                     db="demo_big")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM master_instansi")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[1]

db.close()

print "</body>"
print "</html>" 