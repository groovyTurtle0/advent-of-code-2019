#Puzzle Input
f = open("path\\to\\input.txt", "r")
puzzleinput = f.read()
f.close()

#Split the input into rows of 25
rows = []
for i in range(int(len(puzzleinput)/25)):
	rows.append(puzzleinput[25*i:25*i+25])

#Split the rows into the layers - groups of 6 rows
layers = []
for i in range(int(len(rows)/6)):
	layers.append("".join(rows[6*i:6*i+6]))

#Loop through each layer, counting the zeroes, to find the one with the fewest 0s
fewest0s = 25*6
fewest0layer = None
for l in layers:
	z = l.count("0")
	if z < fewest0s:
		fewest0s = z
		fewest0layer = l

#Print the answer - 1s in that layer * 2s in that layer
print(fewest0layer.count("1")*fewest0layer.count("2"))


#Part 2

#Start at the last layer
final = list(layers[-1])
#Step backwards through the layers
for l in layers[::-1]:
	for i in range(25*6):
		if not (l[i] == "2"):
			#Update the final layer if the cell is not transparent
			final[i] = l[i]
			
#Print out the characters of the final layer
#This just prints 1s and 0s to be used to visualise in another program
final = "".join(final)
for i in range(int(len(final)/25)):
	print(final[25*i:25*i+25])