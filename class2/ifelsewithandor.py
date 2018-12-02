raining=int(input("Is it raining?(0:not raining , 1:raining)"))
holiday=int(input("Do you have a holiday:(0:no holiday,1:holiday)"))
'''
if raining == 0:
    if holiday ==1:
        print("you can jog")
    else:
        print("you canot jog")
else:
    print("you canot jog")

'''


#with 'and' 'or" operators
if raining==0 and holiday ==1:
    print('inside you can jog')
else:
    print("you cannot jog")


