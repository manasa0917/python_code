import mysql.connector
def insertOrder(line):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="python12",
        database="ecomm"
    )
    mycursor = mydb.cursor()
    word_list=line.split(",")

    sql="INSERT INTO orders (phone_no,product_id,quantity) VALUES (%s,%s,%s)"
    val=(word_list[0].strip(),word_list[1].strip(),int(word_list[2].strip()))
    mycursor.execute(sql,val)
    mydb.commit()
with open("order_data.txt","r") as myfile:
    line=myfile.readline()
    while(line):
        try:
            insertOrder(line)
        except:
            continue
        finally:
            line=myfile.readline()

