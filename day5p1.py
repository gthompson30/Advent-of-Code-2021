f = open('inputs/day5.txt', 'r').readlines()
lines = []

grid = [[0 for i in range(1000)] for j in range(1000)]

for line in f:
	a = line[:-1].split(' -> ')
	a = [map(int, i.split(',')) for i in a]
	x1, y1 = a[0]
	x2, y2 = a[1]

	if (x1 == x2):
		for i in range(min(y1, y2), max(y1, y2) + 1):
			grid[i][x1] += 1
	elif (y1 == y2):
		for i in range(min(x1, x2), max(x1, x2) + 1):
			grid[y1][i] += 1

count = 0
for row in grid:
	for column in row:
		if column > 1:
			count += 1

print(count)
