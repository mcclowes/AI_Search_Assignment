from brute_force import brute_force_search
from modified_brute_force import modified_brute_force_search
from nearest_neighbour import nearest_neighbour_search
from genetic import genetic_search
from graph_tools import *

def test_brute_force(name, graph, graphSize):
	print ("Running Brute Force Search...")
	(bruteForceTour, bruteForceTourLength) = brute_force_search(graph, graphSize)
	output_tour(name, graphSize, str(bruteForceTour).strip('()'), bruteForceTourLength)

def test_modified_brute_force(name, graph, graphSize):
	print ("Running Modified Brute Force Search...")
	(bruteForceTour, bruteForceTourLength) = modified_brute_force_search(graph, graphSize)
	output_tour(name, graphSize, str(bruteForceTour).strip('[]'), bruteForceTourLength)

def test_nearest_neightbour(name, graph, graphSize):
	print ("Running Nearest Neighbour Search...")
	(nearestNeighbourTour, nearestNeighbourTourLength) = nearest_neighbour_search(graph, graphSize)
	output_tour(name, graphSize, str(nearestNeighbourTour).strip('[]'), nearestNeighbourTourLength)

def test_genetic(name, graph, graphSize):
	print ("Running Genetic Search...")
	(geneticTour, geneticTourLength) = genetic_search(graph, graphSize)
	output_tour(name, graphSize, str(geneticTour).strip('[]'), geneticTourLength)

def output_tour(name, size, bestTour, bestTourLength):
	with open(str("tour" + name + ".txt"), "w") as tourFile:
		tourFile.write("NAME = " + name + ",\n")
		tourFile.write("TOURSIZE = " + str(size) + ",\n")
		tourFile.write("LENGTH = " + str(bestTourLength) + ",\n")
		tourFile.write(bestTour)

methodList = {"brute": test_brute_force, "modified": test_modified_brute_force, "nearest": test_nearest_neightbour, "genetic": test_genetic}

#Print list of commands
def help():
    print ('\nCommand List:')
    print ('"help": Prints this list\n')
    print ('Search algorithms:')
    print ('- "brute": Runs a true Brute Force Search algorithm on a given graph. Warning: Running for larger graphs will cause problems.')
    print ('- "modified": Runs a Modified Brute Force Search algorithm on a given graph.')
    print ('- "nearest: Runs a Nearest Neighbour Search algorithm on a given graph.')
    print ('- "genetic": Runs a Genetic Search algorithm on a given graph.\n')

#Start search
def start_search():
	help()
	while (1):
		try:
			userInput = (input('\nWhat would you like to do?\n')).lower()
			(name, size, graph) = parse(str(input('\nSelect a graph file to run on (including file suffix).\n')))
			print ('Parsing ' + name + '.txt')
			methodList[userInput](name, graph, size)
			print ("Search completed")
		except:
			print ('\nCommand not recognised.\n')
			help()
			continue

start_search()

