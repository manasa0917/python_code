n=int(input("Enter n:"))
m=int(input("Enter m:"))
tmp = []
result_list=[]
for i in range(0,n):
    tmp=[]
    for j in range(0,m):
        tmp.append(i*j)
    result_list.append(tmp)
print(result_list)

test=[]
test.append(1)
test.append(2)
print(test)
test.clear()
print(test)
