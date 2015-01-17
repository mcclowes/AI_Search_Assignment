from itertools import permutations
from graph_tools import tour_length

#Brute force method
def nearest_neighbour_search(graph, graphSize):
	#Assign starting variables
	bestTourLength = 9999999999 #Replace this!!!!
	bestTour = 0
	tours = []

	for i in range(1, graphSize+1):
		tours.append(search_from_start(i))
		tourLength = tourLength(tours[i-1])
		if tourLength < bestTourLength:
			bestTourLength = tourLength
			bestTour = tours[i]

def search_from_start(graph, startNode):
	
	