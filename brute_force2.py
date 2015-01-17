from itertools import permutations
from graph_tools import tour_length

#Brute force method
def brute_force_search(graph, graphSize):
	#Assign starting variables
	bestTourLength = 9999999999 #Replace this!!!!
	bestTour = 0

	#Find the best tour #Generate all permutations of tours
	for tour in list(permutations(range(1,graphSize+1), graphSize)):
		tourLength = tour_length(tour, graph)
		if  tourLength < bestTourLength:
			bestTour = tour
			bestTourLength = tourLength

	#Return best tour length and the tour
	return (bestTour, bestTourLength)