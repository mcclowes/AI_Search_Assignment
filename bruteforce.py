from itertools import permutations
from graph_tools import tour_length

#Brute force method
def brute_force_search1(graph, graphSize):
	#Generate all permutations of tours
	tours = list(permutations(range(1,graphSize+1), graphSize))

	#Assign starting variables
	bestTourLength = 9999999999 #Replace this!!!!
	bestTour = 0

	#Find the best tour
	for i in range(len(tours)): 
		tourLength = 0

		for j in range(graphSize-1): #Put this counting into a method in graph tools
			tourLength = tourLength + graph[tours[i][j]-1][ tours[i][j+1]-1]
		tourLength = tourLength + graph[tours[i][-1]-1][tours[i][0]-1]

		if tourLength < bestTourLength:
			bestTour = i
			bestTourLength = tourLength

	#Return best tour length and the tour
	return tours[bestTour]
	#return bestTourLength

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
	return tours[bestTour]
	#return bestTourLength