import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="RKCE"
)
c=mydb.cursor()
c.execute("delete from employee where city=vijayawada")
mydb.commit()