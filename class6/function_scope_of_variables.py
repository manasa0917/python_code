#call by value is for Integer Float and String
def modifyInt(a):
    a=20
    return a
def modifyFloat(a):
    a=5.5
    return a

def modifyString(a):
    a=a+"d"
    return a
a=100
print("Before modification a ={}".format(a))
a=modifyInt(a)
print("After modification a ={}".format(a))

#call by reference
def modifyList(mylist):
    mylist.append("modified")
b=[1,2,3]
print("Before modification b ={}".format(b))
modifyList(b)
print("After modification b ={}".format(b))


c="Manasa"
c=modifyString(c)
print(c)
#How to copy and change the list
mylist=[1,2,3]
newlist=mylist.copy()

newlist[0]=100
print(mylist)
print(newlist)
