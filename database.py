# programe to show CRUD function
import mysql.connector as mysql

# connecting with database
connection = mysql.connect(user="root", passwd="root123", host="localhost")
data = connection.cursor()
data.execute("use practical")
# insertinf data into database
data.execute("insert into staff values('sam',1306)")
data.execute("insert into staff values('alen',3005)")
# saving the changes
connection.commit()
# fetching data
data.execute("select * from  staff")
print(data.fetchall())
connection.close()
