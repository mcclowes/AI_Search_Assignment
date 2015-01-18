import re

def parse(fileName):
	readFile = open(fileName, 'r')
	fileString = ""
	for line in readFile:
		fileString = fileString + str(line)
	fileString = re.sub('\s', '', fileString)
	elements = fileString.split(',')

	name = elements[0]
	if re.match("NAME=.+", name):
		name = name[5:]
	else:
		print ("Error: Name cannot be read")

	size = elements[1]
	if re.match("SIZE=\d+", size):
		size = int(size[5:])
	else:
		print ("Error: Size cannot be read")

	elements = elements[2:]
	for element in enumerate(elements):
		elements[element[0]] = int(re.sub('[^\d]', '', element[1]))
		
	graph = [[-1 for x in range(size)] for y in range(size)]
	i = 0
	for x in range(size):
		for y in range(x+1, size):
			graph[x][y] = elements[i]
			graph[y][x] =	graph[x][y]
			i = i +1

	return (name, size,	graph)

#Prints graph line-by-line
def print_graph(graph):
	for item in graph:
		print (item)

#Calculates the length of a given tour
def tour_length(tour, graph):
	tourLength = graph[tour[-1]-1][tour[0]-1] #Initialise with last -> first edge
	for i in range(len(tour)-1):
		tourLength = tourLength + graph[tour[i]-1][ tour[i+1]-1] #Sum rest of edges
	return tourLength

#Calculates the lower bound for a given graph
def lower_bound(inputGraph):
	graph = [] #Copy the graph
	for subList in inputGraph:
		graph.append(subList[:])
	#Remove first node

	#Generate minimum spanning tree

	#Re-add first node

	#return lowerBound

     