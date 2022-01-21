import mysql.connector
from cryptography.fernet import Fernet
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="class"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM user WHERE id=125"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x[1])
  res = bytes(x[1], 'utf-8')
  key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
  cipher_suite = Fernet(key)
  unciphered_text = (cipher_suite.decrypt(res))
  print(unciphered_text) 
  