#file=open("prime_numbers.txt","a")
start=int(input("Enter starting number(>5:"))
end=int(input("Enter a ending number(<100000:"))
primecount=0
output_string=""
for i in range(start,end+1):
    prime=1
    for j in range(2,i-1):
        if (i % j == 0):
            prime = 0
            break

    if prime == 1:
        primecount=primecount+1
        if (primecount%10== 0):
            output_string=output_string+"\n"
        output_string=output_string+" "+str(i)
        #print("{} is prime".format(i))
    else:
        #print("{} is  not prime".format(i))
        pass
print("{} is the count of prime numbers".format(primecount))
print("Total {} prime numbers found.They are given below".format(primecount))
print(output_string)
file=open("prime_number_{}_to_{}.txt".format(start,end),"w")
file.write(output_string)