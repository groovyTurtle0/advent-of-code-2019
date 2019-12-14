#Class for a moon
#Has properties for its x, y, and z position and velocity
#Has methods to apply gravity between itself and another moon, and to apply velocity to istelf
#As properties for its total energy and its 'state' in x, y, or z (a tuple of its position and velocity)
class Moon:
	def __init__(self, xpos, ypos, zpos):
		self.xpos = xpos
		self.ypos = ypos
		self.zpos = zpos
		self.xvel = 0
		self.yvel = 0
		self.zvel = 0
		
	def applyGravity(self, other):
		if self.xpos > other.xpos:
			self.xvel -= 1
		elif self.xpos < other.xpos:
			self.xvel += 1
			
		if self.ypos > other.ypos:
			self.yvel -= 1
		elif self.ypos < other.ypos:
			self.yvel += 1
			
		if self.zpos > other.zpos:
			self.zvel -= 1
		elif self.zpos < other.zpos:
			self.zvel += 1
			
	def applyVelocity(self):
		self.xpos += self.xvel
		self.ypos += self.yvel
		self.zpos += self.zvel
		
	@property
	def totalEnergy(self):
		pot = abs(self.xpos) + abs(self.ypos) + abs(self.zpos)
		kin = abs(self.xvel) + abs(self.yvel) + abs(self.zvel)
		return pot * kin
	
	@property
	def stateX(self):
		return (self.xpos, self.xvel)
		
	@property
	def stateY(self):
		return (self.ypos, self.yvel)
		
	@property
	def stateZ(self):
		return (self.zpos, self.zvel)
	
	def __repr__(self):
		return f"Moon with position <{self.xpos}, {self.ypos}, {self.zpos}> and velocity <{self.xvel}, {self.yvel}, {self.zvel}>"


#Create the moons
moons = [Moon(17, -9, 4), Moon(2, 2, -13), Moon(-1, 5, -1), Moon(4, 7, -7)]

#Move the moons for 1000 steps
steps = 0
while steps < 1000:
	
	#Apply gravity for each pair of moons
	for m1 in moons:
		for m2 in [m for m in moons if m != m1]:
			m1.applyGravity(m2)
			
	#Apply velocity for each moon
	for m in moons:
		m.applyVelocity()
	
	steps += 1

#Print the total energy after the 1000 steps
print(sum([m.totalEnergy for m in moons]))

#Part 2
#Create the moons
moons = [Moon(17, -9, 4), Moon(2, 2, -13), Moon(-1, 5, -1), Moon(4, 7, -7)]
#Sets to store the seen states for each of x, y, and z
xstates = set()
ystates = set()
zstates = set()

#Variables to store the number of steps it took for x, y, or z to loop
xrep = None
yrep = None
zrep = None

#Move the moons as before
steps = 0
while True:

	#Apply gravity for each pair of moons
	for m1 in moons:
		for m2 in [m for m in moons if m != m1]:
			m1.applyGravity(m2)
			
	#Apply velocity for each moon
	for m in moons:
		m.applyVelocity()
	
	#Get the states of each moon
	statex = ()
	statey = ()
	statez = ()
	#Create tuples of the states of each moon concatenated together
	for m in moons:
		statex += m.stateX
		statey += m.stateY
		statez += m.stateZ
	#If we've found a repitition for one of the axes, record it
	if statex in xstates and xrep is None:
		xrep = steps
	if statey in ystates and yrep is None:
		yrep = steps
	if statez in zstates and zrep is None:
		zrep = steps
	#Add the states to the seen states
	xstates.add(statex)
	ystates.add(statey)
	zstates.add(statez)
	
	#Break if we've found repititions for all of x, y, and z
	if not(xrep is None) and not(yrep is None) and not(zrep is None):
		break
	
	steps += 1
	
#Print the number of steps it took for each axes to repeat
#The final answer is the lowest common multiple of these three numbers
print(xrep, yrep, zrep)