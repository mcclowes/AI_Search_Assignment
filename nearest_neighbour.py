from itertools import permutations
from graph_tools import tour_length

#Brute force method
def nearest_neighbour_search(graph, graphSize):
	#Assign starting variables
	bestTourLength = 9999999999 #Replace this!!!!
	bestTour = 0
	tours = []

	for i in range(1, graphSize+1):
		tours.append(search_from_start(graph, graphSize, [i]))
		tourLength = tourLength(tours[i-1])
		if tourLength < bestTourLength:
			bestTourLength = tourLength
			bestTour = tours[i]

def search_from_start(graph, graphSize, tour):
	minDist = 99999999999 #Replace this?
	bestNode = 0
	#Check for shortest dist to next node
	for i in range(graphSize):
		if (graph[tour[-1]][i] <minDist) & (graph[tour[-1]][i] != -1):
			bestNode = i+1
	if bestNode == 0:
		return tour
	#Add next node to tour
	tour.append(bestNode)
	#Change relevant dists to -1
	for i in range(graphSize):
		graph[i][bestNode-1] = -1
	#Recurse
	search_from_start(graph, graphSize, tour)

	return tour