"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""


def search_insert(nums, target):
	n = len(nums)
	left, right = 0, n - 1
	while left <= right:
		mid = left + (right - left) // 2
		if nums[mid] == target:
			return mid
		elif nums[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return left


if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5]
	target = 6
	print(search_insert(arr, target))
