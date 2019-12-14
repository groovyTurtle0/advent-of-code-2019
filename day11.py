#Puzzle Input
f = open("path\\to\\input.txt", "r")
puzzleinput = f.read()
f.close()

#Split the input and turn it into a defaultdict for the intcode
prog = puzzleinput.split(",")
prog = [int(i) for i in prog]
from collections import defaultdict
program = defaultdict(int)
for i in range(len(prog)):
	program[i] = prog[i]

#Import the intcode machine
import intcode

#Part 1

#Create an intcode computer and load it with the program
computer = intcode.Intcode(program)

squareColours = defaultdict(int)
currentSquare = (0, 0)
facing = 0
#Run the robot
while not computer.hasHalted:
	#Give the computer the input of the colour of the current square
	computer.addInput(int(squareColours[currentSquare]))
	#Run the computer to get the outputs of the colour and direction
	colour = computer.run(inputBuffer=True, breakOnOutput=True)
	direction = computer.run(inputBuffer=True, breakOnOutput=True)
	
	#If outputs are None (computer halted instead of producing output), break
	if colour is None or direction is None:
		break
	
	#Update the colour of the current square
	squareColours[currentSquare] = colour
	#Turn from the direciton output
	if direction == 1:
		facing += 1
	else:
		facing -= 1
	facing %= 4
	
	#Step onto the next square
	if facing == 0:
		currentSquare = (currentSquare[0], currentSquare[1]+1)
	elif facing == 1:
		currentSquare = (currentSquare[0]+1, currentSquare[1])
	elif facing == 2:
		currentSquare = (currentSquare[0], currentSquare[1]-1)
	elif facing == 3:
		currentSquare = (currentSquare[0]-1, currentSquare[1])

#Print the answer		
print(len(squareColours.keys()))


#Part 2

#Create a new computer with the program
computer = intcode.Intcode(program)

squareColours = defaultdict(int)
currentSquare = (0, 0)
#Start on a white panel
squareColours[currentSquare] = 1
facing = 0
#Repeat as for part 1
while not computer.hasHalted:
	computer.addInput(int(squareColours[currentSquare]))
	colour = computer.run(inputBuffer=True, breakOnOutput=True)
	direction = computer.run(inputBuffer=True, breakOnOutput=True)
	
	if colour is None or direction is None:
		break
	
	squareColours[currentSquare] = colour
	if direction == 1:
		facing += 1
	else:
		facing -= 1
	facing %= 4
	
	if facing == 0:
		currentSquare = (currentSquare[0], currentSquare[1]+1)
	elif facing == 1:
		currentSquare = (currentSquare[0]+1, currentSquare[1])
	elif facing == 2:
		currentSquare = (currentSquare[0], currentSquare[1]-1)
	elif facing == 3:
		currentSquare = (currentSquare[0]-1, currentSquare[1])

#Get the X and Y boundaries that the robot goes on
minX = min([c[0] for c in list(squareColours.keys())])
maxX = max([c[0] for c in list(squareColours.keys())])
minY = min([c[1] for c in list(squareColours.keys())])
maxY = max([c[1] for c in list(squareColours.keys())])

#Print the final image
for y in range(maxY, minY-1, -1):
	for x in range(minX, maxX+1):
		if squareColours[(x, y)] == 1:
			print(u"\u2588", end="")
		else:
			print(" ",end="")
	print("\n",end="")