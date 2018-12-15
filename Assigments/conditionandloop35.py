
while(True):
    try:
        num_string = input("Enter an integer:")
        num_string=int(num_string)
        print("Its a correct integer")
        print("Success")
        break
    except:
         print("Its not an integer.Please enter correct integer,Enter again")
