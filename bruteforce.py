import re

#Recursive brute force method
def brute_force_search(graph):

	return bestLength

#File reading method
#Takes filename and extracts graph
def read_graph(graphFile):
	inputFile = open('%s' % graphFile, 'r')
	fileName = str(inputFile.readline()).split('=')[1]
	graphSize = str(inputFile.readline()).split('=')[1]
	graph = str(inputFile.readlines())
	#graph = re.findall(r"[\w']+", graph)
	#graph.join()
	#graph = graph.split("'")
	#print (fileName)
	print (fileName)
	#print (graphSize)
	print (graphSize)
	#print (graph)
	print (graph)

    #return graph

#brute_force_search(read_graph("AISearchtestcase.txt"))
read_graph('AISearchtestcase.txt')
