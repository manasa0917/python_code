mystring=input("Enter your input string:")
count=0
output_string=""
for char in mystring:
    if char in "aeiouAEIOU":
        count=count+1
print("There are {} of vowels in {}".format(count,mystring))
start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
for i in range(start,end+1):
    prime=1
    for j in range (2,i-1):
        if (i%j==0):
            prime=0
            break
    if prime==1:
        count=count+1
        output_string=output_string+" "+str(i)
    else:
        pass
print("There are {} between {} and {} and are below:".format(count,start,end))
print("The numbers are {}".format(output_string))

