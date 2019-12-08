#Puzzle Input

f = open("path\\to\\input.txt", "r")
puzzleinput = f.read()
f.close()

#Create a list of the masses from the puzzle input
masses = puzzleinput.split("\n")
#Turn the masses into integers
masses = [int(m) for m in masses]


#Part 1
#Loop through each mass, integer divide it by 3, subtract 2, and add it to the total mass
totalFuel = 0
for m in masses:
	totalFuel += (m//3) - 2

print(totalFuel)


#Part 2
#As befure but repeat the operation for each mass until the fuel calculated is 0
totalFuel = 0
for m in masses:
	fuelRequired = max((m//3) - 2, 0)
	while fuelRequired > 0:
		totalFuel += fuelRequired
		fuelRequired = max((fuelRequired//3) - 2, 0)

print(totalFuel)