
hand = open("regex_sum_25947.txt")

import re
count = 0
total=0

for line in hand:
	line = line.rstrip()
	if re.search('[0-9]+', line):
		x = re.findall('[0-9]+', line)
		for a in x:
			b = int(a)
			total = total+b
			count = count+1

print(count)
print(total)	