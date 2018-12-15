start_range=1500
end_range=2700
output_string=""
for i in range(start_range,end_range+1):
    if (i%7==0) and (i%5==0):

        output_string=output_string+" "+ str(i)
    else:
        pass

print(output_string)


