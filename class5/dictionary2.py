fruits={"orange":"A sweet and sour fruit",
        "apple":"good for health",
        "lemon":"has Vitamin C ",
        "carrot":"used as a salad",
        "mango":"Can be used in may side dishes"}
key=input("Enter fruit you want to search:")
#try and except

try:
    print(fruits[key])
except:
    print("Fruit not found")

#Checking in dictionary
if key in fruits:
    print(fruits[key])
else:
    print("Fruit not found")

val=fruits.get(key)
print(val)
if fruits.get(key)!=None:
    print(fruits[key])
