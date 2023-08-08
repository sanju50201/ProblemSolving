"""
Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected integer.

 

Example 1:

Input: nums = [3,2,1,4]
Output: 2
Explanation: In this example, the minimum value is 1 and the maximum value is 4. Therefore, either 2 or 3 can be valid answers.
Example 2:

Input: nums = [1,2]
Output: -1
Explanation: Since there is no number in nums that is neither the maximum nor the minimum, we cannot select a number that satisfies the given condition. Therefore, there is no answer.
Example 3:

Input: nums = [2,1,3]
Output: 2
Explanation: Since 2 is neither the maximum nor the minimum value in nums, it is the only valid answer. 
"""


def not_max_not_min(arr):
    n = len(arr)

    # since, it should be neither max or min
    if n <= 2:
        return -1

    min_val, max_val = float("inf"), float("-inf")
    mid_val = float("inf")

    for num in arr:
        if num < mid_val:
            min_val, mid_val = num, min_val
        elif num > max_val:
            max_val, mid_val = num, max_val
        elif num < max_val and num > min_val:
            mid_val = num

    return mid_val if mid_val is not None else -1


def not_max(arr):
    if len(arr) <= 2:
        return -1

    return sorted(arr)[-2]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(not_max_not_min(arr))
    print(not_max(arr))
