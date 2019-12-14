#Function to run an intcode program
#Returns the program, pc, and rbase of the program when it finishes, as well as output if set to break on output
#ARGUMENTS:
#program		dict	program to run
#pc				int		pc to start at, default to 0
#rbase			int		relative base at the start, default to 0
#verbose		bool	whether to print each instruction that is run
#inputBuffer	list	list to take input from, if None, take input from user input
#breakOnOutput	bool	if true, program will break after the next output instruction, returning the output and the state of the program
def runProgram(program, pc=0, rbase=0, verbose=False, inputBuffer=None, breakOnOutput=False):
	while True:
		instruction = str(program[pc])
		opcode = int(instruction[-2:])
		parameterModes = instruction[:-2][::-1]+"000"
		if verbose:
			print(instruction, "(", opcode, parameterModes, ")", program[pc+1], program[pc+2], program[pc+3])
		if opcode == 1:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			elif parameterModes[0] == "2":
				p1 = program[rbase + p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			elif parameterModes[1] == "2":
				p2 = program[rbase + p2]
			
			
			if parameterModes[2] == "2":
				program[rbase + p3] = p1 + p2
				if verbose:
					print(f"Adding {p1} to {p2} and storing in {rbase + p3}")
			else:
				program[p3] = p1 + p2
				if verbose:
					print(f"Adding {p1} to {p2} and storing in {p3}")
			pc += 4
		
		elif opcode == 2:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			elif parameterModes[0] == "2":
				p1 = program[rbase + p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			elif parameterModes[1] == "2":
				p2 = program[rbase + p2]
			
			
			if parameterModes[2] == "2":
				program[rbase + p3] = p1 * p2
				if verbose:
					print(f"Multiplying {p1} by {p2} and storing in {rbase + p3}")
			else:
				program[p3] = p1 * p2
				if verbose:
					print(f"Multiplying {p1} by {p2} and storing in {p3}")
			pc += 4
			
		elif opcode == 3:
			p1 = program[pc+1]
			if parameterModes[0] == "2":
				p1 = rbase + p1
			if inputBuffer is None:
				program[p1] = int(input(":"))
			else:
				try:
					program[p1] = inputBuffer.pop()
				except IndexError:
					raise IndexError("No input to take")
			
			if verbose:
				print(f"Taking input and storing in {p1}")
			
			pc += 2
			
		elif opcode == 4:
			p1 = program[pc+1]
			if parameterModes[0] == "0":
				p1 = program[p1]
			elif parameterModes[0] == "2":
				p1 = program[rbase + p1]
			if not breakOnOutput or verbose:
				print(">"+str(p1))
			
			if verbose:
				print(f"Outputting from {p1}")
			
			pc += 2
			
			if breakOnOutput:
				return program, pc, rbase, p1

		elif opcode == 5:
			p1 = program[pc+1]
			p2 = program[pc+2]
			if parameterModes[0] == "0":
				p1 = program[p1]
			elif parameterModes[0] == "2":
				p1 = program[rbase + p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			elif parameterModes[1] == "2":
				p2 = program[rbase + p2]
			
			if p1 != 0:
				pc = p2
				if verbose:
					print(f"{p1} is not 0 so jumping to {p2}")
			else:
				if verbose:
					print(f"{p1} is 0 so not jumping to {p2}")
				pc += 3
			
		elif opcode == 6:
			p1 = program[pc+1]
			p2 = program[pc+2]
			if parameterModes[0] == "0":
				p1 = program[p1]
			elif parameterModes[0] == "2":
				p1 = program[rbase + p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			elif parameterModes[1] == "2":
				p2 = program[rbase + p2]
			
			if p1 == 0:
				pc = p2
				if verbose:
					print(f"{p1} is 0 so jumping to {p2}")
			else:
				pc += 3
				if verbose:
					print(f"{p1} is not 0 so not jumping to {p2}")
			
		elif opcode == 7:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			elif parameterModes[0] == "2":
				p1 = program[rbase + p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			elif parameterModes[1] == "2":
				p2 = program[rbase + p2]
			
			if p1 < p2:
				if parameterModes[2] == "2":
					program[rbase + p3] = 1
					if verbose:
						print(f"{p1} is less than {p2} so storing 1 at {rbase + p3}")
				else:
					if verbose:
						print(f"{p1} is less than {p2} so storing 1 at {p3}")
					program[p3] = 1
			else:
				if parameterModes[2] == "2":
					program[rbase + p3] = 0
					if verbose:
						print(f"{p1} is not less than {p2} so storing 0 at {rbase + p3}")
				else:
					program[p3] = 0
					if verbose:
						print(f"{p1} is not less than {p2} so storing 0 at {p3}")
				
			pc += 4
			
		elif opcode == 8:
			p1 = program[pc+1]
			p2 = program[pc+2]
			p3 = program[pc+3]
			if parameterModes[0] == "0":
				p1 = program[p1]
			elif parameterModes[0] == "2":
				p1 = program[rbase + p1]
			if parameterModes[1] == "0":
				p2 = program[p2]
			elif parameterModes[1] == "2":
				p2 = program[rbase + p2]
			
			if p1 == p2:
				if parameterModes[2] == "2":
					program[rbase + p3] = 1
					if verbose:
						print(f"{p1} is euqal to {p2} so storing 1 at {rbase + p3}")
				else:
					if verbose:
						print(f"{p1} is euqal to {p2} so storing 1 at {p3}")
					program[p3] = 1
			else:
				if parameterModes[2] == "2":
					program[rbase + p3] = 0
					if verbose:
						print(f"{p1} is not equal to {p2} so storing 0 at {rbase + p3}")
				else:
					program[p3] = 0
					if verbose:
						print(f"{p1} is not equal to {p2} so storing 0 at {p3}")
				
			pc += 4
		  
		elif opcode == 9:
			p1 = program[pc+1]
			if parameterModes[0] == "0":
				p1 = program[p1]
			elif parameterModes[0] == "2":
				p1 = program[rbase + p1]
			
			if verbose:
				print(f"Incrementing rbase by {p1}")
			rbase += p1
			
			pc += 2
		  
		elif opcode == 99:
			if breakOnOutput:
				return program, pc, rbase, None
			break
			
		else:
			raise ValueError("Invalid opcode: "+str(opcode))
			
	return program

from collections import defaultdict

#Class for an intcode computer
#PROPERTIES:
#memory			dict	stores the memory of the computer
#ipnutBuffer	list	list to use as an input buffer, FIFO
#pc				int		current program counter of the computer
#rbase			int		current relative base of the computer
#hasHalted		bool	whether the program has halted
#METHODS:
#run - run the computer
#	Arguments:
#		verbose			bool	whether to run the program verbosely
#		inputBuffer		bool	whether to use the computer's input buffer for the input or use user input
#		breakOnOutput	bool	whether to break on the next output instruction and return the output, or run until the program halts
#addInput - adds input to the computer's input buffer
#clearInput - clears the computer's input buffer
class Intcode:
	def __init__(self, mem):
		memory = defaultdict(int)
		for i in range(len(mem)):
			memory[i] = mem[i]
		self.memory = memory
		self.inputBuffer = []
		self.pc = 0
		self.rbase = 0
		self.hasHalted = False
	
	def run(self, verbose=False, inputBuffer=False, breakOnOutput=False):
		if not breakOnOutput:
			if inputBuffer:
				self.memory = runProgram(self.memory, self.pc, self.rbase, verbose, self.inputBuffer)
			else:
				self.memory = runProgram(self.memory, self.pc, self.rbase, verbose)
			self.hasHalted = True
		else:
			if inputBuffer:
				self.memory, self.pc, self.rbase, out = runProgram(self.memory, self.pc, self.rbase, verbose, self.inputBuffer, True)
			else:
				self.memory, self.pc, self.rbase, out = runProgram(self.memory, self.pc, self.rbase, verbose, None, True)
			if out == None:
				self.hasHalted = True
			return out
			
	def addInput(self, inp):
		self.inputBuffer.insert(0, inp)
		
	def clearInput(self):
		self.inputBuffer = []