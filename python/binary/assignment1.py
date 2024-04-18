
# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to
# determine the minimum number of times the original sorted list was rotated to obtain the given list.
# Your function should have the worst-case complexity of O(log N), where N is the length of the list.
# You can assume that all the numbers in the list are unique.
#
# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
#
# We define "rotating a list" as removing the last element of the list and adding it before the first element.
# E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
#
# "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7]

from jovian.pythondsa import evaluate_test_cases, evaluate_test_case
# Brute force solution

def count_rotations_linear(nums):
    position = 0

    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        position += 1

    return 0

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return 0

#  Using the binary search function
def count_rotations_generic(nums):
    def condition(mid):
        if mid > 0 and nums[mid] <= nums[mid - 1]:
            if nums[mid] == nums[mid - 1]:
                return 'left'
            else:
                return 'found'
        elif mid > 0 and nums[mid] < nums[len(nums) - 1]:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(nums) - 1, condition)


# Binary in the function
def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid
        elif mid > 0 and nums[mid] < nums[hi]:
            hi = mid - 1
        else:
            lo = mid + 1
    return 0


tests = [
    {'input': {'nums': [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]}, 'output': 3},
    {'input': {'nums': [4, 5, 6, 7, 8, 1, 2, 3]}, 'output': 5},
    {'input': {'nums': [1, 2, 3, 4, 5, 6]}, 'output': 0},
    {'input': {'nums': [6, 1, 2, 3, 4, 5]}, 'output': 1},
    {'input': {'nums': [2, 3, 4, 5, 6, 1]}, 'output': 5},
    {'input': {'nums': [1, 2, 3, 4]}, 'output': 0},
    {'input': {'nums': []}, 'output': 0},
    {'input': {'nums': [1]}, 'output': 0},
    {'input': {'nums': [1, 3, 6, 7, -1, -1]}, 'output': 4}
]

print(evaluate_test_cases(count_rotations_generic, tests))