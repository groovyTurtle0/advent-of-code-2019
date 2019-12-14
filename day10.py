#Puzzle Input
f = open("path\\to\\input.txt", "r")
puzzleinput = f.read()
f.close()

import math

#Split the input
asteroids = puzzleinput.split("\n")
asteroids = [list(a) for a in asteroids]

#Create a list of tuples of the asteroid coordinates
asteroidCoords = []
for y in range(len(asteroids)):
	for x in range(len(asteroids[0])):
		if asteroids[x][y] == "#":
			asteroidCoords.append((x, y))

#Function to get the simplest ratio of the coordinate pair - basically the gradient, but preserving direction
def simplestRatio(c):
	x, y = c
	g = math.gcd(x, y)
	if g != 0:
		return (int(x/g), int(y/g))
	else:
		return (x, y)


mostSeenNum = 0
mostSeen = None
mostSeenCoords = None
#Loop through each asteroid and count the number of other asteroids that it can see
for a in asteroidCoords:
	seen = list(asteroidCoords)
	for i in range(len(seen)):
		#Simplify the coordinates of each asteroid relative to the current asteroid
		seen[i] = simplestRatio((seen[i][0] - a[0], seen[i][1] - a[1]))
	#The asteroid can only see the closest asteroid for each gradient
	seen = set(seen)
	#It can't see itself
	seen.remove((0, 0))
	num = len(seen)
	#Find the asteroid that can see the most
	if num > mostSeenNum:
		mostSeenNum = num
		mostSeen = a
		mostSeenCoords = seen
#Print the answer
print(mostSeenNum)



#Part 2

#Function to get the angle from vertical of an asteroid
def angleFromVertical(c):
	#I realised I stored the x and y coordinates the wrong way round to begin with
	y, x = c
	a = math.atan2(-y, x)
	if a < 0:
		a = math.pi / 2 - a
	else:
		a = math.pi - a
		a = a + 3*math.pi / 2
	return a % (2*math.pi)
	

#Calculate the angle of all asteroids from the main asteroid
asteroidAngles = {}
for a in mostSeenCoords:
	asteroidAngles[angleFromVertical(a)] = a


#Sort the asteroids by angle
lastVaporised = list(asteroidAngles.keys())
lastVaporised.sort()
#Find the 200th asteroid that is vaporised
lastVaporised = asteroidAngles[lastVaporised[199]]
#Print the answer
print((lastVaporised[1] + mostSeen[1]) * 100 + (lastVaporised[0] + mostSeen[0]))