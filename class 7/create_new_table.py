import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="python12",
    database="mydbtest")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (phone_no VARCHAR(255) PRIMARY KEY ,name VARCHAR(255), address VARCHAR(255),pwd VARCHAR(255),data VARCHAR(255))")