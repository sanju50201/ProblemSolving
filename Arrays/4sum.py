# https://leetcode.com/problems/4sum/

def four_sum(nums, target):
	nums.sort()
	n = len(nums)

	if n < 4:
		return []

	quadruplets = []

	# using the 4 pointers approach

	for i in range(n - 3):
		if i > 0 and nums[i] == nums[i - 1]:
			continue

		for j in range(i + 1, n - 2):
			if j > i + 1 and nums[j] == nums[j - 1]:
				continue

			left = j + 1
			right = n - 1

			while left < right:
				current_sum = nums[i] + nums[j] + nums[left] + nums[right]

				if current_sum == target:
					quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
					while left < right and nums[left] == nums[left + 1]:
						left += 1
					while left < right and nums[right] == nums[right - 1]:
						right -= 1
					left += 1
					right -= 1
				elif current_sum < target:
					left += 1
				else:
					right -= 1
		return quadruplets


if __name__ == "__main__":
	arr = [1, 0, -1, 0, -2, 2]
	target = 0
	print(four_sum(arr, target))
