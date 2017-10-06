import urllib.request, urllib.parse, urllib.error

fhand = urlib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in hand:
	print(line.decode().strip())
