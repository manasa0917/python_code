a=0
b=1
c=0
output_string="{}".format(b)

for i in range(2,50):
    c=a+b
    if c<50:
     output_string=output_string+","+str(c)
     a=b
     b=c
    else:
        pass


print(output_string)
