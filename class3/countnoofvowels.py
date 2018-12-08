mystring=input("Enter a string:")
b=0
for char in mystring:
    if char == ('a' or 'e' or 'i' or 'u'):
        b=b+1

print(b)

#Second way
count=0
for char in mystring:
    if char in "aeiouAEIOU":
        count=count+1
print("There are {} vowels in your iput string".format(count))


