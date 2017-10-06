# 5.2 Write a program that repeatedly prompts a user for integer numbers until
# the user enters 'done'. Once 'done' is entered, print out the largest and
# smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the
# number. Enter 7, 2, bob, 10, and 4 and match the output below. 


#Enter user input and catches if it is valid or not

largest=None
smallest=None

while True:
	try:
		num1=input("Enter an integer: ")
		if num1 == "done" :
			break
		num = int(num1)
		print(num)
		if largest is None or num > largest :
			largest=num
		if smallest is None or num < smallest :
			smallest=num
	except:
		print("Invalid input")

print ("Maximum is", largest)
print("Minimum is", smallest)
