from itertools import permutations

graphSize=8

def createGenerator():
	for i in list(permutations(range(1,graphSize+1), graphSize)):
	    yield i
	
mygenerator = createGenerator() # create a generator
for i in mygenerator:
	print(i)