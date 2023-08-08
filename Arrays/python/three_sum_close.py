# https://leetcode.com/problems/3sum-closest/


def three_sum_closest(nums, target):
	nums.sort()
	n = len(nums)
	closest_sum = float("inf")

	for i in range(n - 2):
		if i > 0 and nums[i] == nums[i - 1]:
			continue

		left = i + 1
		right = n - 1

		while left < right:
			current_sum = nums[i] + nums[left] + nums[right]

			if current_sum == target:
				return target
			elif current_sum < target:
				left += 1
			else:
				right -= 1
			if abs(current_sum - target) < abs(closest_sum - target):
				closest_sum = current_sum
	return closest_sum


if __name__ == "__main__":
	nums = [-1, 2, 1, -4]
	target = 1
	print(three_sum_closest(nums, target))
