d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
result={}
for key in d1:
    result[key]=d1[key]
for key in d2:
    if key in result:
        val1=result[key]
        val2=d2[key]
        result[key]=val1+val2
    else:
        result[key]=d2[key]
print(result)


#another method
mylist=[]
mylist.append(d1)
mylist.append(d2)
result={}
for mydict in mylist:
    for key in mydict:
        if key in result:
            val1=result[key]
            val2=mydict[key]
            result[key]=val1+val2
        else:
            result[key]=mydict[key]
print(result)

