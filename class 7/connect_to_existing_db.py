import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="python12",
    database="mydatabase"
)