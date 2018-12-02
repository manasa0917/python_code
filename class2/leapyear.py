year1=int(input("Please enter a year:"))

if (year1%4)== 0 and  ((year1%100)!= 0 or (year1%400)== 0):
    print("year is a leap year")
else:
    print("not a leap ")


