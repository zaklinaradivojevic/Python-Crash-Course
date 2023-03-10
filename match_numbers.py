import re
x = "My favorite 2 numbers are 12 and 42"
y = re.findall("[0-9]+",x)
print(y)

#find the host name - using find and string slicing
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print(atpos)

appos = data.find("",atpos)
print(appos)

host = data[atpos+1 : appos]
print(host)
