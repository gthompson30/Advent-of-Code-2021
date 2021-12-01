import day1p1

nums = list(map(int, open('inputs/day1.txt').readlines()))
sums = []

for i in range(len(nums) - 2):
	sums.append(sum(nums[i:i+3]))

print(sums)

print(day1p1.get_ans(sums))

