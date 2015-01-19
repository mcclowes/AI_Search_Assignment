from itertools import permutations
from graph_tools import tour_length, lower_bound
from datetime import datetime
from random import shuffle

#Brute force search method
def modified_brute_force_search(graph, graphSize):
	bestTourLength = tour_length(range(1,graphSize+1), graph)
	bestTour = range(1,graphSize+1)
	lowerBound = lower_bound(graph, graphSize)

	startTime = datetime.now() #Start timer
	tour = bestTour
	while (((datetime.now() - startTime).total_seconds()) < (graphSize)): #Until timer reaches n seconds (n = graphSize)
		tourLength = tour_length(tour, graph)
		if  tourLength <= bestTourLength:
			bestTour = tour
			bestTourLength = tourLength
			if  (bestTourLength == lowerBound):
				break #If lower bound is reached
		shuffle(tour)
	return (bestTour, bestTourLength) #Return best tour length and the tour