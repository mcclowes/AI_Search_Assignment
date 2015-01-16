#import re
from itertools import permutations

#Brute force method
def brute_force_search(graph, graphSize):
	tours = list(permutations(range(1,graphSize+1), graphSize))

	print ('Tours: ')
	print (tours)

	#Find the best tour
	#for i in range(len(tours)): 
	#	pass

	#Return the best tour
	#return bestTour