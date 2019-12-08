#Puzzle Input

f = open("path\\to\\input.txt", "r")
puzzleinput = f.read()
f.close()

#Split the puzzle input into a list of integers
program = puzzleinput.split(",")
program = [int(p) for p in program]


#Part 1

#Initialise the addresses 1 and 2 with the given values
program[1] = 12
program[2] = 2

#Loop through each integer in the program
pc = 0
while True:
	#If operation is 1 - addition
	if program[pc] == 1:
		program[program[pc+3]] = program[program[pc+1]] + program[program[pc+2]]
	#If operation is 2 - multiplication
	elif program[pc] == 2:
		program[program[pc+3]] = program[program[pc+1]] * program[program[pc+2]]
	#If operation is 99 - break
	elif program[pc] == 99:
		break
	#Increment the pc by 4 to skip to the next instruction
	pc += 4

#Print the output - the value in the first address
print(program[0])


#Part 2

required = 19690720
program = [int(p) for p in program]

#Repeat the part 1 code to run a program for every possible noun and verb pair
for noun in range(100):
	for verb in range(100):
	
		#Initialise the program with the noun and verb pair currently being tested
		memory = list(program)
		program[1] = noun
		program[2] = verb
		
		#Run the program as above
		pc = 0
		while True:
			if memory[pc] == 1:
				memory[memory[pc+3]] = memory[memory[pc+1]] + memory[memory[pc+2]]
			elif memory[pc] == 2:
				memory[memory[pc+3]] = memory[memory[pc+1]] * memory[memory[pc+2]]
			elif memory[pc] == 99:
				break
			pc += 4
		
		#Check if the required output has been produced, and if so print the noun and verb that produced it and break
		if memory[0] == required:
			print(noun, verb)
			print(100 * noun + verb)
			break