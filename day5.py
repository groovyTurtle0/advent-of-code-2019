#Puzzle Input
f = open("path\\to\\input.txt", "r")
puzzleinput = f.read()
f.close()

#Split program and turn it into integers
program = puzzleinput.split(",")
program = [int(p) for p in program]


#Loop through and run the instructions
pc = 0
while True:
	instruction = str(program[pc])
	#Get the opcode and paramter modes for the instructions
	opcode = int(instruction[-2:])
	parameterModes = instruction[:-2][::-1]+"000"
	#Do the operation of the relevant instruction
	if opcode == 1:
		#Get the paramters
		p1 = program[pc+1]
		p2 = program[pc+2]
		p3 = program[pc+3]
		#Change the paramters based on the paramter modes
		if parameterModes[0] == "0":
			p1 = program[p1]
		if parameterModes[1] == "0":
			p2 = program[p2]
		
		#Perform the operation
		program[p3] = p1 + p2
		
		#Increment the program counter to point to the next instruction
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
		#Get the user input and store it
		program[program[pc+1]] = int(input(":"))
		
		pc += 2
		
	elif opcode == 4:
		p1 = program[pc+1]
		if parameterModes[0] == "0":
			p1 = program[p1]
		#Output what is to be outputted
		print(">"+str(p1))
		
		pc += 2
	
	#Part 2 instructions
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
			program[p3] = 1")
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
			program[p3] = 1)
		else:
			program[p3] = 0
			
		pc += 4
	
	#Break if opcode 99
	elif opcode == 99:
		break