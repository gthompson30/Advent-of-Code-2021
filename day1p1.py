f = list(map(int, open('inputs/day1.txt', 'r').readlines()))

def get_ans(nums):
	count = 0

	for i in range(len(nums) - 1):
		if nums[i + 1] > nums[i]:
			count += 1
	return count

if __name__ == '__main__':
	print(get_ans(f))
