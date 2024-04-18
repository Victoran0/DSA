# Given two strings A and B, find the minimum number of steps required to convert A to B, (each operation is counted
# as 1 step). You have the following 3 operations permitted on a word; insert char, delete char and replace char.

str00 = "intention"
str0 = 'execution'

# test cases: general case, listed above
# No changes required
# all the characters need to be changed
# equal length
# One of the strings is empty
# Only required deletion, only requires addition, only requires insertion


# function signature


def min_step(str1, str2, i1=0, i2=0):
    if i1 == len(str1):
        return len(str2) - i2
    elif i2 == len(str2):
        return len(str1) - i1
    elif str1[i1] == str2[i2]:
        return min_step(str1, str2, i1+1, i2+1)
    else:
        return 1 + min(min_step(str1, str2, i1+1, i2),  # deleted
                       min_step(str1, str2, i1+1, i2+1),  # swap
                       min_step(str1, str2, i1, i2+1))  # inserted

# Memoization version of the function which is more optimal nad takes less time


def min_edit_distance_memo(str1, str2):
    memo = {}

    def recurse(i1, i2):
        key = i1, i2
        if key in memo:
            return memo[key]
        elif i1 == len(str1):
            memo[key] = len(str2) - i2
        elif i2 == len(str2):
            memo[key] = len(str1) - i1
        elif str1[i1] == str2[i2]:
            memo[key] = recurse(i1+1, i2+1)
        else:
            memo[key] = 1 + min(recurse(i1+1, i2), recurse(i1+1, i2+1), recurse(i1, i2+1))
        return memo[key]
    return recurse(0, 0)


test = min_edit_distance_memo('intention', 'execution')
print(test)















