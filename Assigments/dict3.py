mydict={}
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60,7:70,8:80}
mylist=[]
mylist.append(dic1)
mylist.append(dic2)
mylist.append(dic3)

print(mylist)
result={}
for mydict in mylist:
    for key in mydict:
      result[key]=mydict[key]