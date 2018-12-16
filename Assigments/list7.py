mylist=[1,1,2,2,3,3,4,4,5,5,6,6]
mydict={}
for item in mylist:
    mydict[item]="Random stuff"
result=list(mydict.keys())
print(result)
