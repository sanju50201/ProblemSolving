# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def remove_duplicates(nums):
	n = len(nums)
	if n < 2:
		return n
	i = 0
	for j in range(1, n):
		if nums[j] != nums[i]:
			i += 1
			nums[i] = nums[j]
	nums = nums[:i + 1]
	return i + 1


if __name__ == "__main__":
	nums = [1, 2]
	print(remove_duplicates(nums))
