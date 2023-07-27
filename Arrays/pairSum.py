# Given an unsorted integer array, find a pair with the given sum in it.
# Input:
#
# nums = [8, 7, 2, 5, 3, 1]
# target = 10
#
# Output:
#
# Pair found (8, 2)
# or
# Pair found (7, 3)
#
#
# Input:
#
# nums = [5, 2, 6, 8, 1, 9]
# target = 12
#
# Output: Pair not found

# This is one of the solution but this solution has a time complexity of O(n^2)


def find_pair(nums, target):
    # consider each element except the last element
    for i in range(len(nums) - 1):
        # start from the i'th element until the last element
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"Pairs found: {nums[i], nums[j]}")
                return

    print("No Pairs Found!")


# We can use sorting


def find_pair_better(nums, target):
    # let's sort the array
    nums.sort()

    # maintaining two indices low and high
    (low, high) = (0, len(nums)-1)
    # reduce the space of `high` at each iteartion of the loop

    while low < high:
        if nums[low] + nums[high] == target:
            print(f"Pair Found: {nums[low], nums[high]}")
            return
        # increment the low, if the target is less
        # decrement high, if the target is more

        if nums[low] + nums[high] < target:
            low = low + 1
        else:
            high = high - 1

    print("Pairs Not found!")


# We can use Hashing, key-value pairs


def find_pair_hash(nums, target):
    dict = {}

    for i, e in enumerate(nums):
        # check if the pair exists, if the difference is seen before, print the pair

        if target - e in dict:  # this is nothing but complement
            print(f"Pair Found:{(nums[dict.get(target - e)], nums[i])}")
            return

        # store the index of the current element in the dictionary
        dict[e] = i

    print("Pair not Found!")


# find all the pairs in the given array
def find_all_pairs(nums, target):
    dict = {}
    pairs = []

    for i, e in enumerate(nums):
        complement = target - e

        if complement in dict:
            pair = (nums[dict[complement]], nums[i])
            if pair not in pairs and (pair[1], pair[0]) not in pairs:
                pairs.append(pair)

        dict[e] = i

    if pairs:
        for pair in pairs:
            print(f"Pairs found: {pair}")
    else:
        print("No pairs found.")


if __name__ == "__main__":
    arr = [8, 7, 2, 5, 3, 1]
    target = 10
    print("Brute Force Method: ")
    print(find_pair(arr, target))
    print("Sorting Method: ")
    print(find_pair_better(arr, target))
    print("Using Hashing: ")
    print(find_pair_hash(arr, target))
    print("All the Pairs in a given array: ")
    print(find_all_pairs(arr, target))
