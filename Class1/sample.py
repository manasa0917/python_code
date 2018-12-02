pattern=input("Please enter a pattern:")
num=int(input("Please enter a number:"))
extracted_num =int(pattern[0::2])
res=extracted_num * num
print(res)