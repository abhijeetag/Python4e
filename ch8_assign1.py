# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt



fh = open("romeo.txt")
lst = list()
for line in fh:
	words=line.split()
	for i in range(len(words)):
		if len(lst)==0:
			lst.append(words[i])
		else:
			if words[i] in lst:
				continue
			lst.append(words[i])
lst.sort()
print(lst)

