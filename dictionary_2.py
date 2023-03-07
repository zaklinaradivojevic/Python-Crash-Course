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
        #if the key is not there the count is zero
        oldcount = di.get(w,0)  
        print(w, "old",oldcount)
        newcount = oldcount + 1
        di[w] = newcount
        print(w, "new",newcount)
        
print(di)        