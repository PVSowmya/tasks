import csv
import re
import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="demo"
)

mycursor=db.cursor()
regex = r'\b[A-Za-z0-9._%+-]+@[gmail]+\.[A-Z|a-z]{2,}\b'

file = open("data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
result=[]
notvalid=[]

string = ['Name', 'Country', 'Country Code']
integer = ['Age', 'ISO Code', 'Mobile no']
floating=['Income']
boolean=['IS NRI']
mail=['Email id']

for r in csvreader:
    true = 0
    singlerow = {}
    for i in range(len(r)):

        if (header[i] in string):
            if (r[i].isalpha()):
                true += 1
                singlerow[header[i]]=r[i]
        elif (header[i] in integer):
            if (r[i].isalnum()):
                true += 1
                singlerow[header[i]] = r[i]
        elif (header[i] in floating):
            try:
               float(r[i])
               true += 1
               singlerow[header[i]] = r[i]
            except:
                status="invalid"
        elif (header[i] in boolean):
            if (bool(r[i])):
                true += 1
                if(r[i]=='TRUE' or r[i]=='True' or r[i]== 'true' ):
                    singlerow[header[i]] = 1
                else:
                    singlerow[header[i]] = 0
                
        elif (header[i] in mail):
            if (re.fullmatch(regex, r[i])):
                true += 1
                singlerow[header[i]] = r[i]

            else:
                status="false"
    if (true == len(r)):
            result.append(singlerow)
    else:
        notvalid.append(r)

#mycursor.execute("CREATE TABLE people(name VARCHAR(20),age int,country VARCHAR(30),iso_code int,country_code VARCHAR(10),mobile_no VARCHAR(10),income float,is_nri bool,email_id VARCHAR(30))")
#db.commit()
for i in result:
   # mycursor.execute("INSERT INTO  people(name,age,country,iso_code,country_code,mobile_no,income,is_nri,email_id) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s)",
    #(i['Name'],i['Age'],i['Country'],i['ISO Code'],i['Country Code'],i['Mobile no'],i['Income'],i['IS NRI'],i['Email id']))
    db.commit()

print("The list of Invalid Colums")
with open('invalid.csv', 'w', newline='') as student_file:
    writer = csv.writer(student_file)
    
    writer.writerow(header)
   