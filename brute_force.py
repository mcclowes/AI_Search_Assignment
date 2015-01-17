from itertools import permutations
from graph_tools import tour_length

#Brute force search method
def brute_force_search(graph, graphSize):
	#Assign starting variables
	bestTourLength = tour_length(range(1,graphSize+1), graph)
	bestTour = 0

	#Find the best tour
	for tour in permutations(range(1,graphSize+1), graphSize):
		tourLength = tour_length(tour, graph)
		if  tourLength <= bestTourLength:
			bestTour = tour
			bestTourLength = tourLength

	#Return best tour length and the tour
	return (bestTour, bestTourLength)