mydict={1:10,4:90,3:58,9:57}
mylist=list(mydict.keys())
print(mylist)
mylist.sort()
result={}

for item in mylist:
    val=mydict[item]
    result[item]= val
print(result)
