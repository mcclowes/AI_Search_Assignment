from itertools import permutations
from graph_tools import tour_length, lower_bound
#from graph_tools import lowest_bound

#Root method, runs nearest neighbour search starting from each node
def nearest_neighbour_search(graph, graphSize):
	bestTourLength = 9999999999 #Replace this?
	bestTour = 0
	tours = []
	tourLength = 0
	lowerBound = lower_bound(graph, graphSize)

	for i in range(1, graphSize+1):
		tours.append(search_from_start(graph, graphSize, [i]))
		tourLength = tour_length(tours[i-1], graph)
		if tourLength < bestTourLength:
			bestTourLength = tourLength
			bestTour = tours[i-1]
			if bestTourLength == lowerBound:
				break

	return (bestTour, bestTourLength)

#Recursive nearest neighbour search method, recurses from given start to end
def search_from_start(inputGraph, graphSize, tour):
	graph = [] #Copy the graph
	for subList in inputGraph:
		graph.append(subList[:])
	minDist = 99999999999
	bestNode = 0

	for i in range(graphSize): #Mark last added node as visited
		graph[i][tour[-1]-1] = -1

	for i in range(graphSize): #Check for shortest dist to next node
		if (graph[tour[-1]-1][i] < minDist) & (graph[tour[-1]-1][i] != -1): #If last node --> newnode is the best and
			bestNode = i+1
			minDist = graph[tour[-1]-1][i]

	if (bestNode == 0) or (len(tour) == graphSize): #If no more nodes to travel too, break recursion
		return tour

	tour.append(bestNode)
	search_from_start(graph, graphSize, tour) #Recurse

	return tour