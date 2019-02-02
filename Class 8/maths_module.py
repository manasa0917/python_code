def add(a,b):
    return a+b
def factorial(n):
    if (n>10000):
        return 0
    mult=1
    for i in range(1,n+1):
        mult=mult *i
    return mult
def driverFucntion():
    num1 = int(input("num 1: "))
    num2 = int(input("num 2:   "))
    print("sum = {}".format(add(num1,num2)))
    print("Factorial of sum = {}".format(factorial(add(num1,num2))))
if __name__ == "__main__":
    driverFucntion()
