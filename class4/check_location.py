myfile=open("location.txt","r")
location_list=myfile.readlines()
print(location_list)

#for location in location_list:
#    tmp=location.rstrip()
#    print(tmp)

location_list_clean=[]
for location in location_list:
    tmp=location.strip().upper()
    location_list_clean.append(tmp)
print(location_list_clean)



input_location=input("Please enter your location:")
if input_location.strip().upper() in location_list_clean:
    print("Location is correct.We will deliver your order")
else:
    print("location is incorrect.Can't deliver yor order")



