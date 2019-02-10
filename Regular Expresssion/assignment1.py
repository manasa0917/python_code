import re
def checkFileType(line):
    line=line.strip()
    pattern = r"(\.)([t])([x])([t])#";

    p = re.compile(pattern, re.MULTILINE)
    m=p.search(line)
    if m is None:
        print("File {} did not match".format(line))
    else:
        print("FIle {} matched".format(line))
def readFile():
    with open("data.txt","r") as myfile:
      line=myfile.readline()
    while(line):
        flag=checkFileType(line)

        if flag == 1:
            writeToFile(line)

        line = myfile.readline()
def mainFunction():
    readFile()
if __name__ =='__main__':
    mainFunction()
