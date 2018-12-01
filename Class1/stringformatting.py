name=input("Please tell me your name:")
addr=input("Where do you live?:")
data="{} lives in {}".format(name,addr)
print(data)

myoutput="Hello your name is {0} and your address is {1},{2} again my address is {1} and my name is {0}"
myoutput_new = myoutput.format(name,addr,"some random stuff")

print(myoutput)
print(myoutput_new)

#Using indexing and fetching a variable
data2="abcdefghij"
print(data2[4])
print(data2[-6])
print(len(data2))
print(type(data2))
print(type(data2[4]))
a=6
print(float(a))
outstring=data2[2:5]
print(outstring)
outstring=data2[0:-1:2]
print(outstring)
outstring=data2[0:]
print(outstring)
outstring=data2[4:0:-1]
print(outstring)
outstring=data2[9::-1]
print(outstring)
outstring=data2[-1::-1]



