from random import shuffle
from random import randint
from graph_tools import tour_length
from datetime import datetime

#Genetic algorithm
def genetic_search(graph, graphSize):
	#Step 1 : Create initial sorted population
	population = sorted(gen_population(graphSize))
	startTime = datetime.now() #Start timer
	while (((datetime.now() - startTime).total_seconds()) < graphSize): #Until timer reaches n seconds (n = graphSize)
		print ("loop")
		parent1 = []
		parent2 = []
		child1 = []
		child2 = []
		#Step 2 : Choose parents
		print ("stuck here 1")
		(parent1, parent2) = gen_parents(population, graphSize)
		print ("stuck here 2")
		print ("P1: " + str(parent1))
		print ("P2: " + str(parent2))

		#Step 3 : Crossover -> Create children
		(child1, child2) = gen_children(parent1, parent2)

		#Step 4 : Mutate children
		if (randint(1,2) <= 1):
			print ("stuck here 3")
			child1 = gen_mutation(child1)
			child2 = gen_mutation(child2)

		#Check child is bigger than worst population
		#Step 5 : Reduce population
		population = population[:-2]
		#Step 6 : Add children to population
		print ("C1: " + str(child1))
		print ("C2: " + str(child2))

		population.append(child1)
		population.append(child2)
		population = sorted(population)

	print ("Genetic produced -> " + str(population[0]))
	return population[0]

def gen_population(graphSize):
	population =[]
	tour = range(1,graphSize+1)
	for i in range(graphSize):
		shuffle(tour)
		population.append(list(tour))
	print (population)
	return list(population)

def gen_parents(population, graphSize):
	parent1 = []
	parent2 = []
	print("this")
	roll = randint(1,10)
	if (roll >= 1) & (roll <= 4): #first quarter
		parent1 = population[randint(1,graphSize/4)]
		while (parent2 == []) or (parent2 == parent1):
			parent2 = population[randint(1,graphSize/4)]
	elif (roll >= 5) & (roll <= 7): #second quarter
		parent1 = population[randint(graphSize/4, (graphSize/4)*2)]
		while (parent2 == []) or (parent2 == parent1):
			parent2 = population[randint(graphSize/4, (graphSize/4)*2)]
	elif (roll >= 7) & (roll <= 9): #third quarter
		parent1 = population[randint((graphSize/4)*2, (graphSize/4)*3)]
		while (parent2 == []) or (parent2 == parent1):
			parent2 = population[randint((graphSize/4)*2, (graphSize/4)*3)]
	elif (roll == 10): #4th quarter
		parent1 = population[randint((graphSize/4)*3,graphSize-1)]
		while (parent2 == []) or (parent2 == parent1):
			parent2 = population[randint((graphSize/4)*3,graphSize-1)]
	else:
		print("error")
	print ('that')
	return (parent1, parent2)

def gen_children(parent1, parent2):
	child1 = parent1[:5]
	child2 = parent2[:5]
	child1.extend(parent2[5:])
	child2.extend(parent1[5:])
	return (child1, child2)

def gen_mutation(subject):
	mutated = list(subject)
	mutated[0] = subject[-1]
	mutated[-1] = subject[0]
	return mutated