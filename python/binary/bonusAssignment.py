# You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
# You are also given a target number.
# Write a function to find the position of the target number within the rotated list.
# You can assume that all the numbers in the list are unique.
# Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 5

#  analyzing the problem
#  there are two sorted lists in the rotated sorted list, but the amount of time it has been rotated is unknown
# if we go to the middle and the number is the middle number, the middle position is our answer
# If not, if the middle number is smaller than the number we are looking for and the last element in the list is
# also smaller than the number, then our answer is to the left
# else if the middle number is smaller than this number and the last element of the list is larger than it,
# then we go right
# what if the middle number is larger than this number and the last number is smaller than it, we go left
# and if the middle number is larger than the target and that last element is also larger than it, then we check for the
# smallest element in the array and make it our new middle number.
# If the last number is higher, then we go to the right and if it is smaller, then we go to the left
# The loop keeps running until our middle number is this number and its position is our answer

from jovian.pythondsa import evaluate_test_cases

# Test cases;
tests = [
    {'input': {'r_list': [5, 6, 9, 0, 2, 3, 4], 'target': 2}, 'output': 4},
    {'input': {'r_list': [5, 6, 9, 10, 2, 3, 4], 'target': 9}, 'output': 2},
    {'input': {'r_list': [5, 6, 9, 10, 2, 3, 4], 'target': 4}, 'output': 6},
    {'input': {'r_list': [17, 6, 9, 10, 11, 13, 14], 'target': 6}, 'output': 1},
    {'input': {'r_list': [16, 17, 6, 9, 10, 11, 13, 14, 15], 'target': 11}, 'output': 5},
    {'input': {'r_list': [1, 6, 9, 10, 11, 13, 14], 'target': 1}, 'output': 0},
    {'input': {'r_list': [], 'target': 1}, 'output': -1},
    {'input': {'r_list': [4], 'target': 4}, 'output': 0},
    {'input': {'r_list': [4, 7, 8, 9, 3], 'target': 7}, 'output': 1}
]



def find_target_position_linear(r_list, target):
    lo = 0
    hi = len(r_list) - 1
    mid = (lo + hi) // 2
    while lo <= hi:
        if mid > 0 and r_list[mid] < r_list[mid - 1]:
            return mid
        elif mid > 0 and r_list[mid] < r_list[hi]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

    small_number = r_list[mid]
    if small_number == target:
        return small_number
    elif r_list[hi] > target:
        lo = mid + 1
    elif r_list[hi] < target:
        hi = mid - 1



print(evaluate_test_cases(find_target_position_linear, tests))

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l=0
#         h=len(nums)-1
#         m=(l+h)>>1
#         while l<=h:
#             if nums[m]==target:
#                 return m
#             elif nums[m]>=nums[l]: #Left Half of Array
#                 if target<=nums[m] and target>=nums[l]:
#                     h=m-1
#                 else:
#                     l=m+1
#             else: #Right Half of Array
#                 if target>=nums[m] and target<=nums[h]:
#                     l=m+1
#                 else:
#                     h=m-1
#             m=(l+h)>>1
#         return -1