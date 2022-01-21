import mysql.connector
from cryptography.fernet import Fernet
#import base64
#from crypto import AES
#from crypto import Random

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
     database="class"
)

mycursor=mydb.cursor()


#mycursor.execute("CREATE TABLE students(id int,name VARCHAR(20),course VARCHAR(20),email VARCHAR(30), password varchar(20),address VARCHAR(30),gpa float)")

#sql = "INSERT INTO students(id,name,course,email,password,address,gpa) VALUES (%s,%s,%s,%s,%s,%s,%s)"
#val = [(1234,"snehita","sap","snehita@gmail.com",base64.b64encode("snehita123". encode("utf-8")),"Banglore",8.5),(1235,"lasya","Sql","lasya@gmail.com",base64.b64encode("lasya123". encode("utf-8")),"chennai",8.8),(1236,"kavya","php","kavya@gmail.com",base64.b64encode("kavya123". encode("utf-8")),"Hyderabad",8.6),(1237,"pavani",".net","pavani@gmail.com",base64.b64encode("pavani123". encode("utf-8")),"pune",8.9)]
#mycursor.executemany(sql, val)

#mydb.commit()
#print(mycursor.rowcount, "record(s) added")

#print(base64. b64decode(base64.b64encode("snehita123". encode("utf-8"))))
#sql = "DELETE FROM students WHERE id = 1234"
#mycursor.execute(sql)
#mydb.commit()
#print(mycursor.rowcount, "record(s) deleted")


mycursor=mydb.cursor()
#mycursor.execute("create database class")
#mycursor.execute("CREATE TABLE student(id int,name VARCHAR(20),course VARCHAR(20),email VARCHAR(30),gpa float)")
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b"SuperSecretPassword")   #required to be bytes
print(ciphered_text) 
unciphered_text = (cipher_suite.decrypt(ciphered_text))
print(unciphered_text)
password=ciphered_text

sql = "INSERT INTO user (id,password) VALUES (%s,%s)"
val = (127,password)
mycursor.execute(sql, val)
mydb.commit()

#mycursor.execute("SELECT * FROM student")
#myresult = mycursor.fetchall()
#for x in myresult:
  #print(x)

#sql = "UPDATE student SET gpa =8.7 WHERE name = 'pavani'"

#mycursor.execute(sql)

#mydb.commit()

#print(mycursor.rowcount, "record(s) affected")