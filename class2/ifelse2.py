num1=int(input("Please enter number 1:"))
num2=int(input("Please enter number 2:"))
#Sample if else
if num1 > num2:
    print("{}is greater than {}".format(num1,num2))
else:
    print("{} is greater than {}".format(num2,num1))
#Sample if elif (multiple conditons)
if num1 > num2 :
    print("{} is greater than {}".format(num1,num2))
elif num1==num2 :
    print("{} is equal to {}".format(num1,num2))
else:
    print("{} is greater than {}".format(num2, num1))


