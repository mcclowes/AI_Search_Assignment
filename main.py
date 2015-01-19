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
	print (str(generationNumber) + " generations.")
	output_tour(name, size, str(geneticTour).strip('[]'), geneticTourLength)

def output_tour(name, size, bestTour, bestTourLength):
	with open(str("tour" + name + ".txt"), "w") as tourFile:
		tourFile.write("NAME = " + name + ",\n")
		tourFile.write("TOURSIZE = " + str(size) + ",\n")
		tourFile.write("LENGTH = " + str(bestTourLength) + ",\n")
		tourFile.write(bestTour)

#(name, size, graph) = parse('AISearchtestcase.txt') #Parse graph
(name, size, graph) = parse('AISearchfile021.txt')
print ('Parsing '+name+'.txt')

#print (lower_bound(graph, size))

test_modified_brute_force(graph, size)
#test_nearest_neightbour(graph, size)
#test_genetic(graph, size)
print ("Search completed")

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
    while (1):
        try:
            userInput = (input('\nWhat would you like to do?\n')).lower()
            #(name, size, graph) = parse('AISearchfile012.txt')
            (name, size, graph) = parse(input('\nSelect a graph file to run on.\n'))
			#print ('Parsing ' + name + '.txt')
            methodList[userInput](graph, size)
        except:
            print ('\nCommand not recognised.\n')
            help()
            continue

#start_search() #uncomment this

methodList = {"brute": test_brute_force, "modified": test_modified_brute_force, "nearest": test_nearest_neightbour, "genetic": test_genetic}

