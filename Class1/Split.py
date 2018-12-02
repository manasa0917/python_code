pattern=input("Please enter a pattern:")
num=int(input("Please enter a number:"))
extracted_num =int(pattern[0::2])
res=extracted_num * num
print(res)

all_localities="hsr,koramangala,belladur,btm,mg road"
list_localities = all_localities.split(",")
print(list_localities)
locality=input("Please enter your locality")

if locality in all_localities:
    print("This locality is in Bangalore")
else:
    print("This locality is not in Bangalore")