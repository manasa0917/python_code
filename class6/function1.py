def multiply(a1,b1):
    return a1*b1

num1=int(input("Enter a number a:"))
num2=int(input("Enter a number b:"))

result=multiply(num1,num2)
print(result)

def factorial(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res

num=int(input("Enter a number:"))
res=factorial(num)
print("Factorial of {} is {}".format(num,res))