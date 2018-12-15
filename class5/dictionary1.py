fruits={"orange":"A sweet and sour fruit",
        "apple":"good for health",
        "lemon":"has Vitamin C ",
        "carrot":"used as a salad",
        "mango":"Can be used in may side dishes"}
key=input("Enter fruit you want to search:")
print(fruits[key])
try:
    print("{} : {}".format(key,fruits[key]))
except:
    print("Fruit not found")
#fruits["mango"]="Seasonal fruit,very popular"
#print(fruits)

#Looping on a dictionary
for key in fruits.keys():
    print("{} : {}".format(key, fruits[key]))
#Looping on values
for value in fruits.values():
    print(value)



