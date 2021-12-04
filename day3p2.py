lines = open('inputs/day3.txt', 'r').readlines()
lines = [[int(i) for i in line[:-1]] for line in lines]

def commonness(list, col):
	zeros = 0
	ones = 0

	for sub in list:
		if sub[col] == 0:
			zeros += 1
		else:
			ones += 1

	if zeros > ones:
		return [0, 1]
	return [1, 0]

oxygen = lines
for i in range(12):
	common = commonness(oxygen, i)
	oxygen = [line for line in oxygen if line[i] == common[0]]

print(oxygen)

co2 = lines
for i in range(12):
        common = commonness(co2, i)
        co2 = [line for line in co2 if line[i] == common[1]]
        print(co2)
        print(len(co2))

print(co2)
