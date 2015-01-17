from brute_force import brute_force_search
from nearest_neighbour import nearest_neighbour_search
from genetic import genetic_search
from graph_tools import *

def test_brute_force(graph, graphSize):
	(bruteForceTour, bruteForceTourLength) = brute_force_search(graph, graphSize)
	output_tour(name, size, str(bruteForceTour).strip('()'), bruteForceTourLength)

def test_nearest_neightbour(graph, graphSize):
	(nearestNeighbourTour, nearestNeighbourTourLength) = nearest_neighbour_search(graph, graphSize)
	output_tour(name, size, str(nearestNeighbourTour).strip('[]'), nearestNeighbourTourLength)

def test_genetic(graph, graphSize):
	(geneticTour, geneticTourLength, generationNumber) = brute_force_search(graph, graphSize)
	print ("Best tour: " + str(geneticTour) + "\nTour Length: " + str(geneticTourLength)+ "\nGeneration Number: " + str(generationNumber))

def output_tour(name, size, bestTour, bestTourLength):
	with open(str("tour" + name + ".txt"), "w") as tourFile:
		tourFile.write("NAME = " + name + ",\n")
		tourFile.write("TOURSIZE = " + str(size) + ",\n")
		tourFile.write("LENGTH = " + str(bestTourLength) + ",\n")
		tourFile.write(bestTour)

#Parse graph
#(name, size, graph) = parse('AISearchtestcase.txt')
(name, size, graph) = parse('AISearchfile535.txt')
print ('Parsing '+name+'.txt')
print_graph(graph) #Can remove

#test_brute_force(graph, size)
test_nearest_neightbour(graph, size)
#test_genetic(graph, size)
print ("Search completed.")

#Create UI methods
