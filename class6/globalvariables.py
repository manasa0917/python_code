count=0
a=100
def counter1(b):
   global count
   print("Count1 called")
   count=count+1
   b=20
   print(a)
def counter2(c):
    global count
    print("Count2 called")
    count=count+1
    c=200
    print(a)

def printTotalCalls():
      print("Total calls made = {}".format(count))

counter1(20)
counter1(20)
counter1(20)
counter1(20)
counter1(20)

counter2(20)
counter2(20)
counter2(20)

printTotalCalls()
