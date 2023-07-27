# https://leetcode.com/problems/remove-element/

"""

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

> Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
> Return k.


Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


def remove_element(nums, val):
	k = 0
	for i in range(len(nums)):
		if nums[i] != val:
			nums[k] = nums[i]
			k += 1
	return nums[:k]


if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5]
	val = 3
	print(f"Array Before removing val: {val} => {arr}")
	print(f"Array After removing val: {val} => {remove_element(arr, val)}")
