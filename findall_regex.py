import re
line = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("@([^ ]*)", line)#[^ ] mach non blank characters  * mach many of them
print(y)