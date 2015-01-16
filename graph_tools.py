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
		print ("name is ok")
		name = name[5:]
	else:
		print ("name is in-correctly formatted")

	size = elements[1]
	if re.match("SIZE=\d+", size):
		print ("size is ok")
		size = int(size[5:])
	else:
		print ("size is in-correctly formatted")

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

def tour_length(tour):

	return