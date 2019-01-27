import mysql.connector
def insertCustomer(line):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="python12",
        database="ecomm"
    )
    mycursor = mydb.cursor()
    word_list=line.split(",")
    sql="INSERT INTO customers(name,address,phone_no,pwd,data) VALUES (%s,%s,%s,%s,%s)"
    val=(word_list[0].strip(),word_list[1].strip(),word_list[2].strip(),(word_list[3].strip()),(word_list[4].strip()))
    mycursor.execute(sql,val)
    mydb.commit()
with open("customer_data.txt","r") as myfile:
    line=myfile.readline()
    while(line):
        try:
            insertCustomer(line)
        except:
            continue
        finally:
            line=myfile.readline()
