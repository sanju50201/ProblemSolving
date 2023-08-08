# https://leetcode.com/problems/container-with-most-water/

def container_with_more_water(height):
    n = len(height)  # length of the input height

    # we follow the two pointer approach
    left = 0
    right = n - 1

    # used to track the max area found so far
    max_area = 0

    while left < right:
        # formula to calculate the area, the minimum heights of the two vertical lines multiplied by the distance
        # between them
        max_area = max(max_area, min(height[left], height[right]) * (right - left))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(container_with_more_water(height))
