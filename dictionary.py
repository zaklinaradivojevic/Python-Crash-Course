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
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
            print("**NEW**")   
        print(w, di[w])