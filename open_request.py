import urllib.request  
import urllib.error
import urllib.parse

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())
    