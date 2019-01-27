#reading from a file
myfile=open("sample.txt","r")
data=myfile.read()
print(data.split("\n"))
myfile.close()

print("*"*100)
myfile=open("sample.txt","r")
data=myfile.readlines()
print(data)
data2=[]
for char in data:
    char2=char.strip()
    print(char2)
    data2.append(char2)
print(data2)
myfile.close()
print("*"*100)

myfile=open("sample.txt","r")
line=myfile.readline()
while(line):
    print(line)
    line=myfile.readline()
myfile.close()