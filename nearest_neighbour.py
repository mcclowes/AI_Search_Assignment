from itertools import permutations
from graph_tools import tour_length

#Brute force method
def nearest_neighbour_search(graph, graphSize):
	#Assign starting variables
	bestTourLength = 9999999999 #Replace this!!!!
	bestTour = 0
	tours = []
	tourLength = 0

	for i in range(1, graphSize+1):
		tours.append(search_from_start(graph, graphSize, [i]))
		tourLength = tour_length(tours[i-1], graph)
		if tourLength < bestTourLength:
			bestTourLength = tourLength
			bestTour = tours[i-1]

	return (bestTour, bestTourLength)

def search_from_start(graph1, graphSize, tour):
	#Copy the graph
	graph = []
	for subList in graph1:
		graph.append(subList[:])
	minDist = 99999999999
	bestNode = 0

	for i in range(graphSize):
		graph[i][tour[-1]-1] = -1

	#Check for shortest dist to next node
	for i in range(graphSize):
		#print ("Tour: "+str(tour) + " Dist: " + str(graph[tour[-1]-1][i]))
		if (graph[tour[-1]-1][i] < minDist) & (graph[tour[-1]-1][i] != -1):
			#print("Next node --> " + str(bestNode+1))
			bestNode = i+1

	#If no more nodes to travel too
	if (bestNode == 0) or (len(tour) == graphSize):
		return tour

	tour.append(bestNode)
	search_from_start(graph, graphSize, tour)

	return tour