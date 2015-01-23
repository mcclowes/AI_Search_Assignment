from random import shuffle
from random import randint, randrange
from graph_tools import tour_length
from datetime import datetime

#Genetic algorithm main method
def genetic_search(graph, graphSize):
	#Step 1 : Create initial sorted population
	population = sorted(gen_population(graphSize), key = lambda x: tour_length(x, graph))
	startTime = datetime.now() #Start timer

	while (((datetime.now() - startTime).total_seconds()) < (graphSize)): #Until timer reaches n seconds (n = graphSize)
		print (population)
		parent1 = []
		parent2 = []
		child1 = []
		child2 = []
		#Step 2 : Choose parents
		while (parent2 == []) or (parent1 == []) or (parent2 == parent1):
			#print ("eh")
			parent1 = gen_parent(population, graphSize)
			parent2 = gen_parent(population, graphSize)
			print ("P1: " + str(parent1))
			print ("P2: " + str(parent2))

		#Step 3 : Crossover -> Create children
		(child1, child2) = gen_children(parent1, parent2, graphSize)
		#print("here")
		#Step 4 : Mutate children
		if (randint(1, 5) <= 1):
			child1 = gen_mutation(child1, graph)
		if (randint(1, 5) <= 1):
			child2 = gen_mutation(child2, graph)

		#Check child is bigger than worst population and add
		population = population + [child1]
		population = population + [child2]
		print ("C1: " + str(child1))
		print ("C2: " + str(child2) + "\n")
		population = sorted(population, key = lambda x: tour_length(x, graph))
		population = population[:graphSize]
	#print ("Genetic produced -> " + str(population[0]))
	return best_tour(population, graph)

#Generate an initial tours population a given size
def gen_population(graphSize):
	population =[]
	tour = list(range(1,graphSize+1))
	for i in range(graphSize):
		shuffle(tour)
		population.append(list(tour))
	return list(population)

#Selects a parent from population (weighted towards best)
def gen_parent(population, graphSize):
	parent = []
	roll = randint(1,10)
	#print (roll)
	if (roll >= 1) & (roll <= 4): #first quarter
		pRoll = randint(0, int(graphSize/4))
	elif (roll >= 5) & (roll <= 7): #second quarter
		pRoll = randint(int(graphSize/4), int(graphSize/4)*2)
	elif (roll >= 7) & (roll <= 9): #third quarter
		pRoll = randint(int(graphSize/4)*2, int(graphSize/4)*3)
	elif (roll == 10): #4th quarter
		pRoll = randint(int(graphSize/4)*3,graphSize-1)
	else:
		print("error")
	parent = population[pRoll]
	#print ('Parent: ' + str(parent) + "from roll: " + str(pRoll))

	return parent

#Generate 2 children from 2 parents using crossover
def gen_children(parent1, parent2, graphSize):
	#Pass first half of respective parent
	child1 = parent1[:randrange(1,graphSize-2)]
	child2 = parent2[:randrange(1,graphSize-2)]
	
	for node in parent2:
		if node not in child1:
			child1.append(node)
	for node in parent1:
		if node not in child2:
			child2.append(node)
	
	return (child1, child2)

#Mutates a child through tour improvement
def gen_mutation(tour, graph):
	bestTour = list(tour)
	for i in range(len(bestTour)-1):
		tempTour= list(bestTour)
		tempTour[i], tempTour [i+1] = bestTour[i+1], bestTour[i]
		if (tour_length(tempTour, graph) < tour_length(bestTour, graph)):
			bestTour = list(tempTour)
	return bestTour

#Finds the best tour of the population
def best_tour(population, graph):
	bestTourLength = 9999999999
	bestTour = 0
	for tour in population: #For each start node
		tourLength = tour_length(tour, graph)
		if tourLength < bestTourLength:
			bestTour, bestTourLength = tour, tourLength
	return (bestTour, bestTourLength)

