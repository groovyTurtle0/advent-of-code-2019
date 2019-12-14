#Puzzle Input
f = open("path\\to\\input.txt", "r")
puzzleinput = f.read()
f.close()

#Get the program from the input
program = [int(p) for p in puzzleinput.split(",")]

import intcode

#Create an intcode computer for the program
game = intcode.Intcode(program)

#Part 1
#Run the game and count the number of times it outputs tile 2 - the block
numBlocks = 0
while not game.hasHalted:
	x = game.run(breakOnOutput=True)
	y = game.run(breakOnOutput=True)
	tile = game.run(breakOnOutput=True)
	if tile == 2:
		numBlocks += 1
	
print(numBlocks)


#Part 2

#Create a default dict for the display to store the which tile is at which coordinate, defaulting to 0
from collections import defaultdict
display = defaultdict(int)
score = 0

#Dictionary to lookup what character to display for what tile
displayChars = {
	0: " ",
	1: "\u2588",
	2: "#",
	3: "-",
	4: "O"
}

#Function to draw the display from the current global display dictionary
def drawDisplay():
	for y in range(20):
		for x in range(42):
			print(displayChars[display[(x,y)]],end="")
		print()
	print("Score: "+str(score))


import time

numSteps = 0
#Insert coin
program[0] = 2
ballX = 0
paddleX = 0
#Create a new computer with the program
game = intcode.Intcode(program)
#Run the game until its finished
while not game.hasHalted:
	#Give the input for how to move the joystick based on the relative x positions of the ball and paddle
	game.clearInput()
	if ballX > paddleX:
		game.addInput(1)
	elif ballX < paddleX:
		game.addInput(-1)
	else:
		game.addInput(0)
	
	#Run the game to get the outputs of the tile to update
	x = game.run(inputBuffer=True, breakOnOutput=True)
	y = game.run(inputBuffer=True, breakOnOutput=True)
	tile = game.run(inputBuffer=True, breakOnOutput=True)
	#Update the score if needed, or update the display for that x and y
	if x == -1 and y == 0:
		score = tile
	else:
		display[(x, y)] = tile
	
	#Log the new x coordinates of the ball and paddle
	if tile == 4:
		ballX = x
	if tile == 3:
		paddleX = x

	#Optional code to draw the display each frame and wait between frames to animate it
	#drawDisplay()
	#numSteps += 1
	#if numSteps >= 840:
	#	time.sleep(0.1)

#Print the final score
print(score)