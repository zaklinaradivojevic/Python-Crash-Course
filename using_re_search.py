import re

hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^From:" , line): #same as if line startswith("From:") ^ match the start of the line
        print(line)