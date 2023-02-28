fhand = open("notes.txt")
for line in fhand:
    if line.startswith("from"):
        print(line)