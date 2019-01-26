import sys
try:
    f=open('my_file.xtx','r')
except OSErrror as err:
    print('cannot open file')
    print(err)
else:
    print("file random.txt has {} lines".format(len(f.readlines()))
    f.close())