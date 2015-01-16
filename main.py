from bruteforce import brute_force_search
from graph_tools import *

(name, size, matrix) = parse('AISearchtestcase.txt')

print ('Parsing '+name+'.txt')

print_graph(matrix)

bruteForceTour = brute_force_search(matrix, size)
print ("Calculated length: " + str(tour_length(bruteForceTour,matrix)))
#print ("Brute force tour length: "+ str(bruteForceTour))

#Create UI methods