import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.1.28",
    user="root",
    passwd="python12"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")