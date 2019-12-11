#Puzzle Input
f = open("path\\to\\input.txt", "r")
puzzleinput = f.read()
f.close()

#Function to run a program with inputs and return the output - same as day 5 intcode function with minor changes to return output and take input from a list
def runCode(program, inp):
	pc = 0
	inpsTaken = 0
	while True:
		instruction = str(program[pc])
		opcode = int(instruction[-2:])
		parameterModes = instruction[:-2][::-1]+"000"
		if opcode == 1:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			program[p3] = p1 + p2
			pc += 4
		
		elif opcode == 2:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			program[p3] = p1 * p2
			pc += 4
			
		elif opcode == 3:
			program[program[pc+1]] = int(inp[inpsTaken])
			inpsTaken += 1
			
			pc += 2
			
		elif opcode == 4:
			p1 = program[pc+1]
			if parameterModes[0] == "0":
				p1 = program[p1]
			return p1
			
			pc += 2
			
		elif opcode == 5:
			p1 = program[pc+1]
			p2 = program[pc+2]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			if p1 != 0:
				pc = p2
			else:
				pc +=3
			
		elif opcode == 6:
			p1 = program[pc+1]
			p2 = program[pc+2]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			if p1 == 0:
				pc = p2
			else:
				pc +=3
			
		elif opcode == 7:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			if p1 < p2:
				program[p3] = 1
			else:
				program[p3] = 0
				
			pc += 4
			
		elif opcode == 8:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			if p1 == p2:
				program[p3] = 1
			else:
				program[p3] = 0
				
			pc += 4
			
		elif opcode == 99:
			break
			
#Generate the program from the puzzle input
ampProgram = puzzleinput.split(",")
ampProgram = [int(a) for a in ampProgram]

#Generate permutations of phase settings
from itertools import permutations
phasePerms = permutations(range(5))
phases = []
for perm in phasePerms:
	phases.append(perm)

#Run the program with the phase settings and find the best output
maxOut = 0
#Loop through each possible phase setting
for p in phases:
	pA, pB, pC, pD, pE = p
	#Run the code on each amp in turn, passing the output of one into the next
	outA = runCode(ampProgram, [pA, 0])
	outB = runCode(ampProgram, [pB, outA])
	outC = runCode(ampProgram, [pC, outB])
	outD = runCode(ampProgram, [pD, outC])
	outE = runCode(ampProgram, [pE, outD])
	#Find the maximum number that E outputs
	if outE > maxOut:
		maxOut = outE

#Print the answer
print(maxOut)



### PART 2 ###

#Queue class - follows a First In First Out structure, allowing items to be enqueued in one end and dequeued out the other
#Used for the amplifiers' inputs, acting as an input buffer
class Queue:
	def __init__(self):
		self.q = []
	
	def isEmpty(self):
		return len(self.q) == 0
	
	def isFull(self):
		return False
		
	def enQueue(self, item):
		if not self.isFull():
			self.q.append(item)
		
	def deQueue(self):
		if not self.isEmpty():
			return self.q.pop(0)



#Function to run a program for part 2
#Similar to part 1 function, but takes a queue for the input, and a value for the program counter to start from
#Breaks after the output and returns the output and the state of the program at that time
def runCode2(program, inpQ, pc):
	while True:
		instruction = str(program[pc])
		opcode = int(instruction[-2:])
		parameterModes = instruction[:-2][::-1]+"000"
		if opcode == 1:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			program[p3] = p1 + p2
			pc += 4
		
		elif opcode == 2:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			program[p3] = p1 * p2
			pc += 4
			
		elif opcode == 3:
			program[program[pc+1]] = int(inpQ.deQueue())
			
			pc += 2
			
		elif opcode == 4:
			p1 = program[pc+1]
			if parameterModes[0] == "0":
				p1 = program[p1]
			
			pc += 2
			return p1, pc, program, True			
			
		elif opcode == 5:
			p1 = program[pc+1]
			p2 = program[pc+2]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			if p1 != 0:
				pc = p2
			else:
				pc +=3
			
		elif opcode == 6:
			p1 = program[pc+1]
			p2 = program[pc+2]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			if p1 == 0:
				pc = p2
			else:
				pc +=3
			
		elif opcode == 7:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			if p1 < p2:
				program[p3] = 1
			else:
				program[p3] = 0
				
			pc += 4
			
		elif opcode == 8:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			
			if p1 == p2:
				program[p3] = 1
			else:
				program[p3] = 0
				
			pc += 4
			
		elif opcode == 99:
			return None, None, None, False
			


#Amplifier class
class Amplifier:
	def __init__(self, program, name=""):
		#Initialise the amplifier with a program, an empty input queue, and a name
		self.program = program
		self.inputQueue = Queue()
		self.isRunning = False
		self.hasHalted = False
		self.name = name
	
	#Run the amp's program, taking from the input, and breaking after the output
	def run(self):
		if self.isRunning:
			self.output, self.pc, self.program, self.isRunning = runCode2(self.program, self.inputQueue, self.pc)
			self.hasHalted = not(self.isRunning)
			return self.output
		else:
			self.output, self.pc, self.program, self.isRunning = runCode2(self.program, self.inputQueue, 0)
			return self.output
	
	#Take input and add it to the input queue
	def takeInput(self, inp):
		self.inputQueue.enQueue(inp)
		

#Generate new phase settings
phasePerms = permutations(range(5,10))
phases = []
for perm in phasePerms:
	phases.append(list(perm))

biggestEout = 0
#Loop through all phase settings
for p in phases:
	#Create the amps
	ampA = Amplifier(list(ampProgram), "A")
	ampB = Amplifier(list(ampProgram), "B")
	ampC = Amplifier(list(ampProgram), "C")
	ampD = Amplifier(list(ampProgram), "D")
	ampE = Amplifier(list(ampProgram), "E")
	amps = [ampA, ampB, ampC, ampD, ampE]
	#Give the amps the phase setting input
	for i in range(5):
		amps[i].takeInput(p[i])
	#Give amp A the input 0 to start it off
	ampA.takeInput(0)

	#Run the amps until all have broken
	ampEouts = []
	broken = [False]*5
	currentAmp = 0
	while set(broken) != {True}:
		amp = amps[currentAmp]
		#If the amp has not halted, run the amp
		if not amp.hasHalted:
			out = amp.run()
			#If its amp E, add its output to the list of outputs
			if currentAmp == 4 and out is not None:
				ampEouts.append(out)
			#Give the next amp the input of the output produced by the current amp
			amps[(currentAmp+1)%5].takeInput(out)
		else:
			broken[currentAmp] = True
		
		#Go to the next amp
		currentAmp += 1
		currentAmp %= 5
	
	#Compare the last output of E
	lastEout = ampEouts[-1]
	if lastEout > biggestEout:
		biggestEout = lastEout

#Print the biggest output of E of all the phase settings
print(biggestEout)