while(True):
    try:
        num=int(input("Please enter a number "))
        res=100/num
        print("Result is :{}".format(res))
        break
    except ZeroDivisionError:
        print("You divided by zero")
        continue
    except ValueError:
        print("Not an integer")
        continue
    except BaseException:
        print("some error")
        continue

