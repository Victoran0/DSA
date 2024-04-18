# You are working on a new feature on Jovian called "Top notebooks of the week". Write a function to sort a list of
# notebooks in decreasing order of likes. Keep in mind that up to millions of notebooks can be created every week,
# so your function needs to be as efficient as possible

import random
from jovian.pythondsa import evaluate_test_cases, evaluate_test_case


def bubble_sort(nums):
    # Create a copy of the list to avoid changing it
    nums = list(nums)

    # 4. Repeat the process n-1 times
    for _ in range(len(nums) - 1):
        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):

            # 2. Compare the number with
            if nums[i] > nums[i+1]:

                # 3. swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]

    # Return the sorted list
    return nums


def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums


def merge(nums1, nums2):
    # List to store the results
    merged = []

    # Indices for iteration
    i, j = 0, 0

    # loop over the two lists
    while i < len(nums1) and j < len(nums2):

        # Include the smaller element in the result and move to the next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    # Return the final merged array
    return merged + nums1_tail + nums2_tail


def merge_sort(nums):
    # Terminating condition (List of 0 or 1 elements)
    if len(nums) <= 1:
        return nums

    # Get the midpoint
    mid = len(nums) // 2

    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]

    # Solve the problem for each halves recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # Combine the results of the two halves
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums


def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1

    # initialize right and left pointers
    l, r = start, end-1

    # iterate while they're apart
    while r > l:
        # print('  ', nums, l, r)
        # increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1

        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1

        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end


def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums


class Notebook:
    def __init__(self, title , username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)


def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'


def default_compare(x, y):
    if x < y:
        return 'less'
    elif x == y:
        return 'equal'
    else:
        return 'greater'


def merge_sort_dc(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge_dc(merge_sort_dc(objs[:mid], compare), merge_sort_dc(objs[mid:], compare), compare)


def merge_dc(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]


def compare_titles(nb1, nb2):
    if nb1.title < nb2.title:
        return 'lesser'
    elif nb1.title == nb2.title:
        return 'equal'
    elif nb1.title > nb2.title:
        return 'greater'


def compare_usernames(nb1, nb2):
    if nb1.username < nb2.username:
        return 'lesser'
    elif nb1.username == nb2.username:
        return 'equal'
    elif nb1.username > nb2.username:
        return 'greater'


# list of numbers in random order
test0 = {'input': {'nums': [4, 2, 6, 3, 4, 6, 2, 1]}, 'output': [1, 2, 2, 3, 4, 4, 6, 6]}
# List of numbers in random order
test1 = {'input': {'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]}, 'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]}
# A list that's already sorted
test2 = {'input': {'nums': [3, 5, 6, 8, 9, 10, 99]}, 'output': [3, 5, 6, 8, 9, 10, 99]}
# A list that's sorted in descending order
test3 = {'input': {'nums': [99, 10, 9, 8, 6, 5, 3]}, 'output': [3, 5, 6, 8, 9, 10, 99]}
# A list containing repeating elements
test4 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}
# An empty list
test5 = {'input': {'nums': []}, 'output': []}
# A list containing just one element
test6 = {'input': {'nums': [23]}, 'output': [23]}
# A list containing one element repeated many times
test7 = {'input': {'nums': [42, 42, 42, 42, 42, 42, 42]}, 'output': [42, 42, 42, 42, 42, 42, 42]}

# A list containing so much element
in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]

# Sample notebooks
nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)
notebooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]

print(merge_sort_dc(notebooks, compare_usernames ))
