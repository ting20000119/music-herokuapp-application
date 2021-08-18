import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="je191919",
  database="bts"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name) VALUES ('Jacky')"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")