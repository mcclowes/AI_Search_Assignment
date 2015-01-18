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
	for elem in enumerate(elements):
		elements[elem[0]] = int(re.sub('[^\d]', '', elem[1]))
		
	matrix = [[-1 for x in range(size)] for y in range(size)]
	i = 0
	for x in range(size):
		for y in range(x+1, size):
			matrix[x][y] = elements[i]
			matrix[y][x] = matrix[x][y]
			i = i +1

	return (name, size, matrix)

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

def minimum_spanning_tree(graph):
	#Return the minimum spanning tree of an undirected graph G.
    #G should be represented in such a way that iter(G) lists its
    #vertices, iter(G[u]) lists the neighbors of u, G[u][v] gives the
    #length of edge u,v, and G[u][v] should always equal G[v][u].
    #The tree is returned as a list of edges.
    
    if not isUndirected(G):
        raise ValueError("MinimumSpanningTree: input is not undirected")
    for u in G:
        for v in G[u]:
            if G[u][v] != G[v][u]:
                raise ValueError("MinimumSpanningTree: asymmetric weights")

    # Kruskal's algorithm: sort edges by weight, and add them one at a time.
    # We use Kruskal's algorithm, first because it is very simple to
    # implement once UnionFind exists, and second, because the only slow
    # part (the sort) is sped up by being built in to Python.
    subtrees = UnionFind()
    tree = []
    for W,u,v in sorted((G[u][v],u,v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u,v))
            subtrees.union(u,v)
    return tree      