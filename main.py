from brute_force import brute_force_search
from modified_brute_force import modified_brute_force_search
from nearest_neighbour import nearest_neighbour_search
from genetic import genetic_search
from graph_tools import *

def test_brute_force(graph, graphSize):
	print ("Running Brute Force Search...")
	(bruteForceTour, bruteForceTourLength) = brute_force_search(graph, graphSize)
	output_tour(name, size, str(bruteForceTour).strip('()'), bruteForceTourLength)

def test_modified_brute_force(graph, graphSize):
	print ("Running Modified Brute Force Search...")
	(bruteForceTour, bruteForceTourLength) = modified_brute_force_search(graph, graphSize)
	output_tour(name, size, str(bruteForceTour).strip('()'), bruteForceTourLength)

def test_nearest_neightbour(graph, graphSize):
	print ("Running Nearest Neighbour Search...")
	(nearestNeighbourTour, nearestNeighbourTourLength) = nearest_neighbour_search(graph, graphSize)
	output_tour(name, size, str(nearestNeighbourTour).strip('[]'), nearestNeighbourTourLength)

def test_genetic(graph, graphSize):
	print ("Running Genetic Search...")
	(geneticTour, geneticTourLength, generationNumber) = brute_force_search(graph, graphSize)
	print ("Best tour: " + str(geneticTour) + "\nTour Length: " + str(geneticTourLength)+ "\nGeneration Number: " + str(generationNumber))

def output_tour(name, size, bestTour, bestTourLength):
	with open(str("tour" + name + ".txt"), "w") as tourFile:
		tourFile.write("NAME = " + name + ",\n")
		tourFile.write("TOURSIZE = " + str(size) + ",\n")
		tourFile.write("LENGTH = " + str(bestTourLength) + ",\n")
		tourFile.write(bestTour)

#(name, size, graph) = parse('AISearchtestcase.txt') #Parse graph
(name, size, graph) = parse('AISearchfile012.txt')
print ('Parsing '+name+'.txt')

#test_brute_force(graph, size)
test_modified_brute_force(graph, size)
#test_nearest_neightbour(graph, size)
#test_genetic(graph, size)
print ("Search completed")

#Create UI methods, as in TCP assignment
