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

tmp = list()
for k,v in di.items():
    #print(k, v)
    newtuple = (v, k)
    tmp.append(newtuple)
    
print("Flipped", tmp)    
# top 5 common words in the file    
tmp = sorted(tmp, reverse=True) 
print("Sorted", tmp[:5])   

for k,v in tmp[:5]:
    print(k,v)
