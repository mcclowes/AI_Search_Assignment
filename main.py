from bruteforce import brute_force_search
from graph_parser import parse

(name, size, matrix) = parse('AISearchtestcase.txt')

print ('Parsing '+name+'.txt')

print(matrix)

brute_force_search(matrix, size)
