#Puzzle Input
f = open("path\\to\\input.txt", "r")
puzzleinput = f.read()
f.close()

#Split the orbits by newline
orbitList = puzzleinput.split("\n")

#Class for a body - store pointers to its parent (the body its orbiting) and its children (the bodies that orbit it)
class Body:
	def __init__(self, p=None):
		self.parent = p
		self.children = []
	
	#Method to add a child to the body
	def addChild(self, c):
		self.children.append(c)
		
	@property
	def numChildren(self):
		return len(self.children)


#Generate dictionary of empty bodies so they can be looked up from their names
bodies = {}
bodies["COM"] = Body()
for orbit in orbitList:
	name = orbit[4:]
	bodies[name] = Body()

#Update the parents and childrens of the bodies depending on the orbits
for orbit in orbitList:
	outer = orbit[4:]
	inner = orbit[:3]
	bodies[outer].parent = bodies[inner]
	bodies[inner].addChild(bodies[outer])

#Count the number of direct and indirect orbits
total = 0
def countOrbits(b, i):
	global total
	#Add to the total the number of children the current body has multiplied by how far it is from the centre of mass (to account for the indirect orbits)
	total += b.numChildren * i
	#Recursively count the number of orbits for the children
	for c in b.children:
		countOrbits(c, i+1)

#Start counting the orbits from the COM, then output the reults
countOrbits(bodies["COM"], 1)
print(total)


#Part 2

start = bodies["YOU"].parent
end = bodies["SAN"].parent

#Find the bodies between santa and the COM
santaPath = [end]
current = end
while current != bodies["COM"]:
    current = current.parent
    santaPath.append(current)

#Find the first body in santa's path to the COM, climbing up from YOU
currentLength = 0
current = start
while not current in santaPath:
    current = current.parent
    currentLength += 1

#Print the distance
total = currentLength + santaPath.index(current)
print(total)