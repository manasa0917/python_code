number=int(input("Enter a guess:"))
guesscorrect=0
for i in range(1,9+1):
    if i==number:
        print("{} is Correct guess".format(number))
        guesscorrect=1
        break
if guesscorrect==0:
    print("{} is wrong guess".format(number))
else:
    pass
