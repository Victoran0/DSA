#  Question: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number.

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else :
            lo = mid + 1
    return -1

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return 'left'
            else:
                return 'found'
        else:
            if nums[mid] < target:
                return 'right'
            else:
                return 'left'

    return binary_search(0, len(nums) - 1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return 'right'
            else:
                return 'found'
        else:
            if nums[mid] < target:
                return 'right'
            else:
                return 'left'

    return binary_search(0, len(nums) - 1, condition)

