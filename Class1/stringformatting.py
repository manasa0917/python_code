name=input("Please tell me your name:")
addr=input("Where do you live?:")
data="{} lives in {}".format(name,addr)
print(data)

myoutput="Hello your name is {0} and your address is {1},{2} again my address is {1} and my name is {0}"
myoutput_new = myoutput.format(name,addr,"some random stuff")

print(myoutput)
print(myoutput_new)

