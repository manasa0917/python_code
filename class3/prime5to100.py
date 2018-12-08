start=int(input("Enter starting number(>5:"))
end=int(input("Enter a ending number(<100000:"))
primecount=0
for i in range(start,end+1):
    prime=1
    for j in range(2,i-1):
        if (i % j == 0):
            prime = 0
            break

    if prime == 1:
        primecount=primecount+1
        print("{} is prime".format(i))
    else:
        print("{} is  not prime".format(i))
print("{} is the count of prime numbers".format(primecount))