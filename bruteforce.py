from itertools import permutations
from graph_tools import tour_length

#Brute force method
def brute_force_search(graph, graphSize):
	#Generate all permutations of tours
	tours = list(permutations(range(1,graphSize+1), graphSize))

	#Assign starting variables
	bestTourLength = 9999999999 #Replace this!!!!
	bestTour = 0

	#Find the best tour
	for i in range(len(tours)): 
		tourLength = tour_length(tours[i], graph)
		if  tourLength < bestTourLength:
			bestTour = i
			bestTourLength = tourLength

	#Return best tour length and the tour
	return (tours[bestTour], bestTourLength)