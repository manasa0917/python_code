a=[156,157,189,90]
x=max(a)
print(x)
y=min(a)
print(y)

#another way to find maximum of a list
#max=sys.minsize
import sys
mylist=[39,24,50,200,70,1]
max= -sys.maxsize-1
for item in mylist:
    if item > max:
        max=item
print(max)