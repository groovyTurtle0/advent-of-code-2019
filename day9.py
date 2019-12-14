#Puzzle Input
f = open("path\\to\\input.txt", "r")
puzzleinput = f.read()
f.close()

#Split the puzzle input into the program
prog = puzzleinput.split(",")
prog = [int(p) for p in prog]

#Turn the program into a defaultdict so that memory addresses beyond the end of the program can be referenced, and default to 0
from collections import defaultdict
program = defaultdict(int)
for i in range(len(prog)):
	program[i] = prog[i]

#Step through each instruction and run it depending on the opcode
debug = False
pc = 0
rbase = 0
while True:
	#Unpack the instruction into the opcode and parameter modes
	instruction = str(program[pc])
	opcode = int(instruction[-2:])
	parameterModes = instruction[:-2][::-1]+"000"
	if debug:
		print(instruction, "(", opcode, parameterModes, ")", program[pc+1], program[pc+2], program[pc+3])
	#Depending on the opcode, perform the appropriate operation
	if opcode == 1:
		#Get the parameters for the instruction
		p1 = program[pc+1]
		p2 = program[pc+2]
		p3 = program[pc+3]
		#Check the parameter modes for the parameters
		if parameterModes[0] == "0":
			p1 = program[p1]
		elif parameterModes[0] == "2":
			p1 = program[rbase + p1]
		if parameterModes[1] == "0":
			p2 = program[p2]
		elif parameterModes[1] == "2":
			p2 = program[rbase + p2]
		
		if debug:
			print(f"Adding {p1} to {p2} and storing in {p3}")
		
		#Perform the operation
		if parameterModes[2] == "2":
			program[rbase + p3] = p1 + p2
		else:
			program[p3] = p1 + p2
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
		
		if debug:
			print(f"Multiplying {p1} by {p2} and storing in {p3}")
		
		if parameterModes[2] == "2":
			program[rbase + p3] = p1 * p2
		else:
			program[p3] = p1 * p2
		pc += 4
		
	elif opcode == 3:
		p1 = program[pc+1]
		if parameterModes[0] == "2":
			p1 = rbase + p1
			if debug:
				print(rbase, p1)
		program[p1] = int(input(":"))
		
		if debug:
			print(f"Taking input and storing in {p1}")
		
		pc += 2
		
	elif opcode == 4:
		p1 = program[pc+1]
		if parameterModes[0] == "0":
			p1 = program[p1]
		elif parameterModes[0] == "2":
			p1 = program[rbase + p1]
		print(">"+str(p1))
		
		if debug:
			print(f"Outputting from {p1}")
		
		pc += 2
		
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
			if debug:
				print(f"{p1} is not 0 so jumping to {p2}")
		else:
			if debug:
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
			if debug:
				print(f"{p1} is 0 so jumping to {p2}")
		else:
			pc += 3
			if debug:
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
				if debug:
					print(f"{p1} is less than {p2} so storing 1 at {rbase + p3}")
			else:
				if debug:
					print(f"{p1} is less than {p2} so storing 1 at {p3}")
				program[p3] = 1
		else:
			if parameterModes[2] == "2":
				program[rbase + p3] = 0
				if debug:
					print(f"{p1} is not less than {p2} so storing 0 at {rbase + p3}")
			else:
				program[p3] = 0
				if debug:
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
				if debug:
					print(f"{p1} is euqal to {p2} so storing 1 at {rbase + p3}")
			else:
				if debug:
					print(f"{p1} is euqal to {p2} so storing 1 at {p3}")
				program[p3] = 1
		else:
			if parameterModes[2] == "2":
				program[rbase + p3] = 0
				if debug:
					print(f"{p1} is not equal to {p2} so storing 0 at {rbase + p3}")
			else:
				program[p3] = 0
				if debug:
					print(f"{p1} is not equal to {p2} so storing 0 at {p3}")
			
		pc += 4
	
	#Operation to increment the relative base
	elif opcode == 9:
		p1 = program[pc+1]
		if parameterModes[0] == "0":
			p1 = program[p1]
		elif parameterModes[0] == "2":
			p1 = program[rbase + p1]
		
		if debug:
			print(f"Incrementing rbase by {p1}")
		rbase += p1
		
		pc += 2
	  
	elif opcode == 99:
		break