a=['abc','xyz','bab','1221']
count=0
for item in a:
    if len(item)> 2 and item[-1]==item [0]:
        count=count+1
print(count)
