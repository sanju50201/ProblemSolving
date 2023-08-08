"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""


def search_range(nums, target):
	n = len(nums)
	left, right = 0, n - 1
	start, end = -1, -1

	# first binary search to find the first position of the target
	while left <= right:
		mid = left + (right - left) // 2

		if nums[mid] == target:
			start = mid
			right = mid - 1
		elif nums[mid] < target:
			left = mid + 1
		else:
			right = mid - 1

	# if the target is not found, then return [-1, -1]
	if start == -1:
		return [-1, -1]

	# reset the first and last positions for the second binary search, to find the last occurrence
	left, right = 0, n - 1

	while left <= right:
		mid = left + (right - left) // 2

		if nums[mid] == target:
			end = mid
			left = mid + 1
		elif nums[mid] < target:
			left = mid + 1
		else:
			right = mid - 1

	return [start, end]


if __name__ == "__main__":
	arr = [5, 7, 7, 8, 8, 10]
	target = 8
	print(search_range(arr, target))
