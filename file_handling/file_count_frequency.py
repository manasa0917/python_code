frequency={}

def calculateFrequency(line):
    global frequency
    word_list = line.split(",")
    print(word_list)
    for word in word_list:
        temp=word.strip()
        print(temp)
        if temp in frequency:
            val=frequency[temp]
            val=val+1
            frequency[temp]=val
        else:
            frequency[temp] = 1


with open("sample.txt","r") as myfile:
    line=myfile.readline()
    while(line):
        calculateFrequency(line)
        line=myfile.readline()
print(frequency)