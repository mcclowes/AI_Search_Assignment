from brute_force3 import brute_force_search
from graph_tools import *

def test_brute_force(graph, graphSize):
	(bruteForceTour, bruteForceTourLength) = brute_force_search(graph, graphSize)
	print ("Best tour: " + str(bruteForceTour) + "\nTour Length: " + str(bruteForceTourLength))

def test_nearest_neightbour(graph, graphSize):
	(nearestNeighbourTour, nearestNeighbourTourLength) = nearest_neighbour_search(graph, graphSize)
	print ("Best tour: " + str(bruteForceTour) + "\nTour Length: " + str(bruteForceTourLength))

def test_genetic(graph, graphSize):
	(geneticTour, geneticTourLength, generationNumber) = brute_force_search(graph, graphSize)
	print ("Best tour: " + str(geneticTour) + "\nTour Length: " + str(geneticTourLength)+ "\nGeneration Number: " + str(generationNumber))

#Main
#Parse graph
(name, size, graph) = parse('AISearchtestcase.txt')
#(name, size, graph) = parse('AISearchfile012.txt')
print ('Parsing '+name+'.txt')
print_graph(graph)

test_brute_force(graph, size)
#test_nearest_neightbour(graph, size)
print ("Calculation completed.")

#Create UI methods