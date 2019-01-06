dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
mydict={}
for key in dict1:
    mydict[key]=dict1[key]
for key in dict2:
    mydict[key]=dict2[key]
for key in dict3:
    mydict[key]=dict3[key]
print(mydict)
mydict[7]=70
print(mydict)


mylist=[]
mylist.append(dict1)
mylist.append(dict2)
mylist.append(dict3)
print(mylist)
result={}
for mydict in mylist:
    for key in mydict:
        result[key]= mydict[key]
        print(result[key])
print(result)

