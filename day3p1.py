length = 12

# definitely already exists in python
def to_dec(n):
        total = 0
        length = len(n)

        for i, x in enumerate(n):
                total += int(x) * (2 ** (length - 1 - i))

        return total

lines = open('inputs/day3.txt', 'r').readlines()
lines = [i[:-1][::-1] for i in lines]
zeros = [0 for i in range(length)]
ones  = [0 for i in range(length)]

for i in range(0, length):
	current0 = 0
	current1 = 0
	for line in lines:
		if line[i] == '1':
			current1 += 1
		else:
			current0 += 1
	zeros[i] = current0
	ones[i] = current1

out = ''
zeros = zeros[::-1]
ones = ones[::-1]
for i in range(length):
	if zeros[i] > ones[i]:
		out += '0'
	else:
		out += '1'

print(zeros)
print(ones)

print(to_dec(out))
