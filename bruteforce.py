#import re
from itertools import permutations

#Brute force method
def brute_force_search(graph, graphSize):
	tours = list(permutations(range(1,graphSize+1), graphSize))

	bestTourLength = 0
	bestTour = 0

	#Find the best tour
	for i in range(len(tours)): 
		tourLength = 0
		for j in range(graphSize-1):
			print (str(i) + " " + str(j))
			tourLength = tourLength + graph[tours[i][j]-1][ tours[i][j+1]-1]
		tourLength = tourLength + graph[tours[i][-1]-1][tours[i][0]-1]

		if tourLength > bestTourLength:
			bestTour = i
			bestTourLength = tourLength

	temp.append(tours[bestTour])
	#Return best tour length and the tour
	return temp