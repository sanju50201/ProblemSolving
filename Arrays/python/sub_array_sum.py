# Given an integer array, check if it contains a subarray having zero-sum.


# Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

# Output: Subarray with zero-sum exists

# The subarrays with a sum of 0 are:

# { 3, 4, -7 }
# { 4, -7, 3 }
# { -7, 3, 1, 3 }
# { 3, 1, -4 }
# { 3, 1, 3, 1, -4, -2, -2 }
# { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

def has_zero_sum_sub(nums):
    if sum(nums) == 0:
        return True

    s = set()
    s.add(0)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            s.add(nums[i] + nums[j])

    # return True is 0 is in the set.
    return 0 in s


if __name__ == "__main__":
    arr = [4, -6, 3, -1, 4, 2, 7]
    if has_zero_sum_sub(arr):
        print("Sub List Exists")
    else:
        print("Sublist doesn't exist...")
