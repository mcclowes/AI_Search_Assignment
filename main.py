from bruteforce import brute_force_search
from graph_tools import *

#(name, size, matrix) = parse('AISearchtestcase.txt')
(name, size, matrix) = parse('AISearchfile012.txt')

print ('Parsing '+name+'.txt')

print_graph(matrix)

(bruteForceTour, bruteForceTourLength) = brute_force_search(matrix, size)
print ("Calculated length: " + str(bruteForceTour) + "\nTour Length: " + str(bruteForceTourLength))

print ("Calculation completed.")
#Create UI methods