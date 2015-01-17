from itertools import permutations
from graph_tools import tour_length

#Permutations generator
def createGenerator(graphSize):
	for i in list(permutations(range(1,graphSize+1), graphSize)):
	    yield i

#Brute force method
def brute_force_search(graph, graphSize):
	#Assign starting variables
	bestTourLength = 9999999999 #Replace this!!!!
	bestTour = 0
	tourgenerator = createGenerator(graphSize) # create a generator
	print ("Got here!")
	for tour in tourgenerator:
		tourLength = tour_length(tour, graph)
		if  tourLength < bestTourLength:
			bestTour = tour
			bestTourLength = tourLength
	#Return best tour length and the tour
	return (bestTour, bestTourLength)