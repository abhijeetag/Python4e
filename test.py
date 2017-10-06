d = {'a':10, 'b':1, 'c':22} 
l = list()
for key in d.items() : 
	l.append( (val, key) )
print(l)