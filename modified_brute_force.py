from itertools import permutations
from graph_tools import tour_length, lower_bound
from datetime import datetime

#Brute force search method
def modified_brute_force_search(graph, graphSize):
	bestTourLength = tour_length(range(1,graphSize+1), graph)
	bestTour = 0
	lowerBound = lower_bound(graph, graphSize)

	startTime = datetime.now() #Start timer
	for tour in permutations(range(1,graphSize+1), graphSize): #Find the best tour
		tourLength = tour_length(tour, graph)
		if  tourLength <= bestTourLength:
			bestTour = tour
			bestTourLength = tourLength
		if ((datetime.now() - startTime).total_seconds()) > (graphSize) or (bestTourLength == lowerBound):
			break #If timer reaches n seconds, break (n = graphSize)

	return (bestTour, bestTourLength) #Return best tour length and the tour