#Range to search through (from puzzle input)
minimum = 178416
maximum = 676461

#Function to return if a string has at least one pair of two adjacent digits
def twoAdj(s):
	#Loop through each character in the string
	for c in range(len(s)-1):
		#If the character is the same as the next character, there is a block of 2, so return True
		if s[c] == s[c+1]:
			return True
	#If no blocks of two were found, return False
	return False

#Function to return if the number never decreases as you step along the digits
def dec(s):
	last = 0
	#Compare each digit to the previous one to see if it breaks the rule
	for c in s:
		if int(c) < last:
			return False
		last = int(c)
	#If nothing breaks the rule, return False
	return True

#Function for part 2 - if number has a block of length exactly 2
def twoAdjOnly(s):
	#For each digit 0 - 9, return true if it appears twice and not more than twice
	for i in range(10):
		if str(i)*2 in s and not str(i)*3 in s:
			return True
	#If no digit satisfies this condition, return False
	return False

#Part 1 - loop through the range to search and increment the count for each number that matches the criteria
count = 0
for n in range(minimum, maximum+1):
	if twoAdj(str(n)) and dec(str(n)):
		count += 1
		
print(count)


#Part 2 - as above but with twoAdjOnly instead of twoAdj
count = 0
for n in range(minimum, maximum+1):
	if twoAdjOnly(str(n)) and dec(str(n)):
		count += 1
		
print(count)