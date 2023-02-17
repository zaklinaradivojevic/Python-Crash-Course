# Get the name of the file and open it
name = input('Enter file:')
handle = open(name)

# Create an empty dictionary
counts = {}
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
