import mysql.connector
def getData(phone_no):
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        passwd="yourpassword",
        database="mydbtest"
    )
    mycursor = mydb.cursor()
    sql= "SELECT * from customers where phone_no = phone_no"
    mycursor.execute(sql)

def insert(sql,val):
    mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabase"
    )
    mycursor = mydb.cursor()

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
def createNewUser():
    phone_no = input("Phone No :")
    name=input("Name:")
    address=input("Address:")
    pwd=input("password")
    data=input("Tell me about youself:")
    sql="INSERT INTO customers (phone_no,name, address,pwd,data) VALUES (%s, %s,%s,%s,%s)"
    val=(phone,no,name,address,pwd,data)
    insert(sql,val)

def loginAndShowData():
    phone_no=input("Phone No:")
    pwd=input("password:")
    value=getdata(phone_no)
    value=value1[0]
    print(value)
    stored_pwd=value[3]
    if (stored_pwd == pwd):
        print("login success")
        print(value[4])

choice=int(input("Sign up (1) or Login (2)"))

if choice == 1 :
    createNewUser()
else:
    loginAndShow()
