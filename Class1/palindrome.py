mystring = input("please input a string?:")
reverse = mystring[-1::-1]
if reverse == mystring:
   print("Input String is a Palindrome")
else:
   print("Input String is not a Palindrome")
print("it is a palindrome")


data=input("Enter the input:")
reverse2=data[len(data)-1::-1]
reverse2=data[-1:-1]
if reverse2==data:
    print("input string {} is a palindrome".format(data))


else:
    print("input string is not a palindrome")
print("goodbye")