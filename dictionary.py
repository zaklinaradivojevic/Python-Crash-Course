fname = input("Enter file: ")
if len(fname) < 1: fname = "intro.txt"
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds:
        print(w)
        if w in di:
            di[w] = di[w] + 1
            print("**Existing**")
        else:
            di[w] = 1
            print("**NEW**")   
        print(di[w])