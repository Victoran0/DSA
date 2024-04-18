# Given am array of positive numbers, find the continous subarray that adds up to a number.

def subarray_sum1(arr, target):
    n = len(arr)
    # i goes from 0 to n-1
    for i in range(0, n):
        # j goes from i to n
        for j in range(i, n+1):
            # check if subarray sum equal target
            if (sum(arr[i:j])) == target:
                # answer found
                return i, j
    return None, None


# Optimization; maintain a running sum for inner loop, when sum exceeds target, break inner loop

def subarray_sum2(arr, target):
    n = len(arr)
    # i goes from 0 to n-1
    for i in range(0, n):
        s = 0 # running sum
        for j in range(i, n+1):
            if s == target:
                return i, j
            elif s > target:
                break
            if j < n:
                s += arr[j]

    return None, None


# Optimization; we can keep moving our subarray forward or backward not necessarily we increment i and start again from
# scratch, we can move i by 1 when the subarray we have is greater than 10, and we can move j also.

def subarray_sum3(arr, target):
    n = len(arr)
    i, j, s = 0, 0, 0
    while i < n and j < n+1:
        if s == target:
            return i, j
        elif s < target:
            if j < n:
                s += arr[j]
            j += 1
        elif s > target:
            s -= arr[i]
            i += 1
    return None, None


arr0 = [3, 5, 1, 2, 6, 7]
target0 = 16

print(subarray_sum3(arr0, target0))







