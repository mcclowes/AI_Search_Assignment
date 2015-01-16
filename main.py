from bruteforce import brute_force_search
from graph_tools import *

(name, size, matrix) = parse('AISearchtestcase.txt')

print ('Parsing '+name+'.txt')

print(matrix)

bruteForceTour = brute_force_search(matrix, size)
print (tour_length(bruteForceTour))
print (bruteForceTour)