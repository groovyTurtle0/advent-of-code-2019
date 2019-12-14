#Puzzle Input
f = open("path\\to\\input.txt", "r")
puzzleinput = f.read()
f.close()

import math

#Class to store a reaction, with an tuple of what product it outputs, and a list of tuples of its reactants
class Reaction:
	def __init__(self, line):
		line = line.split(" => ")
		
		output = line[1].split(" ")
		self.output = (output[1], int(output[0]))
		
		input = line[0].split(", ")
		self.input = []
		for i in input:
			i = i.split(" ")
			self.input.append((i[1], int(i[0])))
			

#Create the reactions from the puzzle input
reactions = {}
for r in puzzleinput.split("\n"):
	r = Reaction(r)
	reactions[r.output[0]] = r


required = [("FUEL", 1)]
inventory = {}
oreTotal = 0
#Loop through all required ingredients until no more are required
while len(required) > 0:
	next = required.pop(0)
	#If the required ingredient is ore, add it to the total ore required
	if next[0] == "ORE":
		oreTotal += next[1]
		continue
	
	#Find the reaction required to produce the current ingredient
	reaction = reactions[next[0]]
	
	numRequired = next[1]
	#If we already have some of the required ingredient, take it away from how much we need
	if next[0] in inventory.keys():
		if inventory[next[0]] > numRequired:
			inventory[next[0]] -= numRequired
			continue
		else:
			numRequired -= inventory[next[0]]
			inventory[next[0]] = 0
	
	#Calculate the number of times we need to perform the reaction
	numReactions = math.ceil(numRequired / reaction.output[1])
	
	#Add any exces produced to the inventory
	excess = reaction.output[1] * numReactions - numRequired
	if next[0] in inventory.keys():
		inventory[next[0]] += excess
	else:
		inventory[next[0]] = excess
	
	#Add to the list of required ingredients all of the ingredients required to perform this reaction
	for ingredient in reaction.input:
		#If its already in the list of required ingredients, update it, otherwise append it
		if ingredient[0] in [i[0] for i in required]:
			required[[i[0] for i in required].index(ingredient[0])] = (ingredient[0], ingredient[1]*numReactions + required[[i[0] for i in required].index(ingredient[0])][1])
		else:
			required.append((ingredient[0], ingredient[1]*numReactions))

#Print the answer
print(oreTotal)

#Part 2
#Function to do as above, finding the minimum amount of ore required for any amount of fule
def oreForFuel(target):
	required = [("FUEL", target)]
	inventory = {}
	oreTotal = 0
	while len(required) > 0:
		next = required.pop(0)
		
		if next[0] == "ORE":
			oreTotal += next[1]
			continue

		reaction = reactions[next[0]]
		
		numRequired = next[1]
		if next[0] in inventory.keys():
			if inventory[next[0]] > numRequired:
				inventory[next[0]] -= numRequired
				continue
			else:
				numRequired -= inventory[next[0]]
				inventory[next[0]] = 0
		
		numReactions = math.ceil(numRequired / reaction.output[1])
		
		excess = reaction.output[1] * numReactions - numRequired
		if next[0] in inventory.keys():
			inventory[next[0]] += excess
		else:
			inventory[next[0]] = excess
		
		for ingredient in reaction.input:
			if ingredient[0] in [i[0] for i in required]:
				required[[i[0] for i in required].index(ingredient[0])] = (ingredient[0], ingredient[1]*numReactions + required[[i[0] for i in required].index(ingredient[0])][1])
			else:
				required.append((ingredient[0], ingredient[1]*numReactions))
		
	return oreTotal
	
#Narrow down on the amount of fuel that can be created with 1tn units of ore
lowerBound = 1
upperBound = 10000000
while upperBound > lowerBound + 1:
	#Test the middle of the lower and upper bounds to see how much ore is needed to create that much fuel, until the amount of ore required is 1tn
	nextTest = int((upperBound+lowerBound)/2)
	thisOre = oreForFuel(nextTest)
	if thisOre < 1000000000000:
		lowerBound = nextTest
	elif thisOre > 1000000000000:
		upperBound = nextTest
	else:
		break
#Print the answer
print(lowerBound)