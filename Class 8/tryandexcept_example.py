while(True):
    try:
        num=int(input("Please enter a number b/w 1 to 10"))
        if num >= 1 and num <= 10:
            print("Correct ")
            break
        else:
            continue
    except:
        continue

