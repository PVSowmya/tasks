import mysql.connector
from cryptography.fernet import Fernet

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="demo"
)

mycursor=db.cursor()

key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
cipher_text = Fernet(key)
ciphered_text = cipher_text.encrypt(b"niha123")   #required to be bytes
#print(ciphered_text) 
unciphered_text = (cipher_text.decrypt(ciphered_text))
#print(unciphered_text)
password=ciphered_text

#mycursor.execute("CREATE TABLE students(id int,name VARCHAR(20),course VARCHAR(20),email VARCHAR(30), password varchar(20),address VARCHAR(30),gpa float)")
#db.commit()

#sql = "INSERT INTO students(id,name,course,email,password,address,gpa) VALUES (%s,%s,%s,%s,%s,%s,%s)"
#val = [1239,"niha","niha","niha@gmail.com",password,"pune",8.6]
#mycursor.execute(sql, val)
#db.commit()
#print(mycursor.rowcount, "record(s) added")

#mycursor.execute("SELECT * FROM students")
#myresult = mycursor.fetchall()
#for x in myresult:
  #print(x[3])

sql = "SELECT * FROM students WHERE id =1237"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  #print(x[4])
  res = bytes(x[4], 'utf-8')
  key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
  cipher_text = Fernet(key)
  unciphered_text = (cipher_text.decrypt(res))
  plain_text=bytes(unciphered_text).decode("utf-8")
  print(plain_text) 