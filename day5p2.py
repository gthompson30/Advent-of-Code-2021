f = open('inputs/day5test.txt', 'r').readlines()
lines = []

grid = [[0 for i in range(10)] for j in range(10)]

def draw_diaganol(board, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0:
                dx = 0
        elif dx > 0:
                dx = 1
        else:
                dx = -1
        if dy == 0:
                dy = 0
        elif dy > 0:
                dy = 1
        else:
                dy = -1

        x = x1
        y = y1
        while (x != x2 + dx and y != y2 + dy):
                board[y][x] += 1
                x += dx
                y += dy

        return board

for line in f:
	a = line[:-1].split(' -> ')
	a = [map(int, i.split(',')) for i in a]
	x1, y1 = a[0]
	x2, y2 = a[1]
	grid = draw_diaganol(grid, x1, y1, x2, y2)

count = 0
for row in grid:
	for column in row:
		if column > 1:
			count += 1

print(count)
