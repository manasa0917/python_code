import re
pattern =r"([a-z]+)|([1-9]+)";

p = re.compile(pattern,re.MULTILINE)
m=p.findall("1234asd")
print(m)