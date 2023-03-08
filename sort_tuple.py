fhand = open("romeo.txt")
counts = dict()
for line in fhand :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
lst = list()
for key, val in counts.items():
     newtup = (val,key) 
     lst.append(newtup) 
     
lst = sorted(lst, reverse=True)# the value that is higest is gona be the first
#print 10 most common words in a file
for val, key in lst[:10]:
    print(key, val)
                       