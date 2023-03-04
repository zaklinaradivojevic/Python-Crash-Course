fname = input("Enter file: ")
if len(fname) < 1: fname = "intro.txt"
hand = open(fname)

for line in hand:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds:
        print(w)