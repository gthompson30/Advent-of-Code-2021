f = open('inputs/day4.txt', 'r')

moves = list(map(int, f.readline().split(',')))
boards = []

for i in range(100):
	f.readline()
	boards.append([])
	for j in range(5):
		boards[i].append(list(map(int, f.readline().strip().split())))

def is_bingo(board):
	for i in range(5):
		# yes i know this is not good
		if board[0][i] and board[1][i] and board[2][i] and board[3][i] and board[4][i]:
			return True
	for i in range(5):
		if board[i].count(True) == 5:
			return True
	return False

def index2d(array, item):
	for row, list in enumerate(array):
		for col, current in enumerate(list):
			if current == item:
				return (row, col)
	return -1

def calc_score(board, bools, just_called):
	total = 0
	for i, row in enumerate(board):
		for j, item in enumerate(row):
			if bools[i][j] == False:
				total += item
	return total * just_called

min_count = 0
min_board = []
n = []
score = 0

for board in boards:
	count = 0
	correct = [[False for i in range(5)] for i in range(5)]
	for move in moves:
		index = index2d(board, move)
		if index != -1:
			correct[index[0]][index[1]] = True
		if is_bingo(correct):
			if count > min_count:
				min_board = board
				min_count = count
				n = correct
				score = calc_score(board, correct, move)
			break
		count += 1

print(score)
#print(min_count)
#print(n)

