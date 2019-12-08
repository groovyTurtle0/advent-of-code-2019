#Open the puzzle input file
f = open("path\\to\\input.txt","r")
puzzleInput = f.read().split("\n")
f.close()

#Split the inputs for each wire
wire1 = puzzleInput[0].split(",")
wire2 = puzzleInput[1].split(",")

#Initialise signals dicts for part 2
signals1 = {}
signals2 = {}

#Part 1
#Generate list of squares visited by wire 1

wire1squares = []
currentSquare = [0, 0]
currentSignal = 0
#Loop through each joint in the wire
for joint in wire1:
	#Determine the direction to go in and the distance to go for from the joint
    direction = joint[0]
    length = int(joint[1:])
	#Depending on the direction, increment or decrement either the x or y coordinate of the current square
    if direction == "R":
        for i in range(length):
            currentSquare[0] += 1
            currentSignal += 1
            wire1squares.append(tuple(currentSquare))
			#For part 2 - add the signal for this square to the signal dict, and set it if its already there
            try:
                if signals1[tuple(currentSquare)] > currentSignal:
                    signals1[tuple(currentSquare)] = currentSignal
            except:
                signals1[tuple(currentSquare)] = currentSignal
    elif direction == "L":
        for i in range(length):
            currentSquare[0] -= 1
            currentSignal += 1
            wire1squares.append(tuple(currentSquare))
            try:
                if signals1[tuple(currentSquare)] > currentSignal:
                    signals1[tuple(currentSquare)] = currentSignal
            except:
                signals1[tuple(currentSquare)] = currentSignal
    elif direction == "U":
        for i in range(length):
            currentSquare[1] += 1
            currentSignal += 1
            wire1squares.append(tuple(currentSquare))
            try:
                if signals1[tuple(currentSquare)] > currentSignal:
                    signals1[tuple(currentSquare)] = currentSignal
            except:
                signals1[tuple(currentSquare)] = currentSignal
    elif direction == "D":
        for i in range(length):
            currentSquare[1] -= 1
            currentSignal += 1
            wire1squares.append(tuple(currentSquare))
            try:
                if signals1[tuple(currentSquare)] > currentSignal:
                    signals1[tuple(currentSquare)] = currentSignal
            except:
                signals1[tuple(currentSquare)] = currentSignal


#Generate list of squares visited by wire 2            
#As above, but for wire 2
wire2squares = []
currentSquare = [0, 0]
currentSignal = 0
for joint in wire2:
    direction = joint[0]
    length = int(joint[1:])
    if direction == "R":
        for i in range(length):
            currentSquare[0] += 1
            wire2squares.append(tuple(currentSquare))
            currentSignal += 1
            try:
                if signals2[tuple(currentSquare)] > currentSignal:
                    signals2[tuple(currentSquare)] = currentSignal
            except:
                signals2[tuple(currentSquare)] = currentSignal

    elif direction == "L":
        for i in range(length):
            currentSquare[0] -= 1
            currentSignal += 1
            wire2squares.append(tuple(currentSquare))
            try:
                if signals2[tuple(currentSquare)] > currentSignal:
                    signals2[tuple(currentSquare)] = currentSignal
            except:
                signals2[tuple(currentSquare)] = currentSignal

    elif direction == "U":
        for i in range(length):
            currentSquare[1] += 1
            currentSignal += 1
            wire2squares.append(tuple(currentSquare))
            try:
                if signals2[tuple(currentSquare)] > currentSignal:
                    signals2[tuple(currentSquare)] = currentSignal
            except:
                signals2[tuple(currentSquare)] = currentSignal

              
    elif direction == "D":
        for i in range(length):
            currentSquare[1] -= 1
            currentSignal += 1
            wire2squares.append(tuple(currentSquare))
            try:
                if signals2[tuple(currentSquare)] > currentSignal:
                    signals2[tuple(currentSquare)] = currentSignal
            except:
                signals2[tuple(currentSquare)] = currentSignal

#Find intersections
#Convert the lists into sets, and use the & operator to find the intersection of the sets (much faster than looping through lists)
intersections = set(wire1squares) & set(wire2squares)

#Part 1 output - minimum manhattan distance of all intersections
print(min(abs(i[0]) + abs(i[1]) for i in intersections))

#Part 2 output - minimum sum of signals of all intersections
print(min([signals1[i] + signals2[i] for i in intersections]))

#Random turtle to draw the wires
'''
import turtle
turtle.goto(0,0)
turtle.color('red')
turtle.ht()
turtle.speed(0)
for joint in wire1:
    direction = joint[0]
    length = int(joint[1:])/50
    if direction == "R":
        turtle.seth(90)
    elif direction == "L":
        turtle.seth(270)
    elif direction == "U":
        turtle.seth(0)
    elif direction == "D":
        turtle.seth(180)
    turtle.forward(length)

turtle.pu()
turtle.goto(0,0)
turtle.color('blue')
turtle.ht()
turtle.speed(0)
turtle.pd()
for joint in wire2:
    direction = joint[0]
    length = int(joint[1:])/50
    if direction == "R":
        turtle.seth(90)
    elif direction == "L":
        turtle.seth(270)
    elif direction == "U":
        turtle.seth(0)
    elif direction == "D":
        turtle.seth(180)
    turtle.forward(length)
 '''