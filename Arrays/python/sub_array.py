# Given an integer array, print all subarrays with zero-sum.

# For example,

# Input:  { 4, 2, -3, -1, 0, 4 }

# Subarrays with zero-sum are

# { -3, -1, 0, 4 }
# { 0 }


# Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

# Subarrays with zero-sum are

# { 3, 4, -7 }
# { 4, -7, 3 }
# { -7, 3, 1, 3 }
# { 3, 1, -4 }
# { 3, 1, 3, 1, -4, -2, -2 }
# { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

# using brute force solution

def print_sub_lists(nums):
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]

            if total == 0:
                print(f"Sublist: {i, j}")


if __name__ == "__main__":
    arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -21, 2, 3,]
    print(print_sub_lists(arr))
