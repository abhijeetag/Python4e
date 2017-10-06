# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fhand=open('mbox-short.txt')

counts=dict()

for line in fhand:
	words=line.split()
	if len(words) == 0 : continue
	if words[0]=="From":
		# print(words[5])
		tperiods = words[5].split(':')
		hour=tperiods[0]
		# print(hour)
		if hour not in counts:
			counts[hour] = 1
		else:
			counts[hour] += 1			

for w in sorted(counts):
  print(w, counts[w])