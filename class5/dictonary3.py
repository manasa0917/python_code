def findKey(val):
    fruits = {"orange": "A sweet and sour fruit",
              "apple": "Good for health",
              "lemon": "Has Vitamin C ",
              "carrot": "Used as a salad",
              "mango": "Best summer fruit"}
    for key in fruits:
        if val==fruits[key]:
            return key

fruits={"orange":"A sweet and sour fruit",
        "apple":"Good for health",
        "lemon":"Has Vitamin C ",
        "carrot":"Used as a salad",
        "mango":"Best summer fruit"}

listofkeys=list(fruits.keys())
print(listofkeys)
listofkeys.sort()

for key in listofkeys:
    print("{} : {}".format(key,fruits[key]))
#sorting based on value ,create another list of list
listofvalues=list(fruits.values())
listofvalues.sort()
print(listofvalues)
final_list=[]

for val in listofvalues:
    tmp = []
    key=findKey(val)
    tmp.append(key)
    tmp.append(val)
    final_list.append(tmp)

print(final_list)
