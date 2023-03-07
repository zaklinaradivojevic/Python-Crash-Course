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
        #idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        #print(w, "new", di[w])
        
print(di)  

#now we wont to find the most common word
# k is key
# v is value
largest = -1
theword = None
for k,v in di.items() :
    print(k,v)
    if v > largest :
        largest = v
        theword = k #capture/remember the key that was  largest
        
print("Done", theword, largest)        