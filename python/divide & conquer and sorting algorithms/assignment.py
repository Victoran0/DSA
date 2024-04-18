# Given two polynomials represented by two lists, write a function that efficiently multiplies
# given two polynomials. For example, the lists [2, 0, 5, 7] and [3, 4, 2] represent the
# polynomials 2 + 5x2 + 7x3 and 3 + 4x + 2x2
# Their product is 6 + 8x + 19x2 + 41x3 + 38x4 + 14x5
# It can be represented by the list [6, 8, 19, 41, 38, 14].

def multiply_polynomials(poly1, poly2):
    length = len(poly1) + len(poly2) - 1
    result = [0] * length
    for k in range(length):
        i, j = 0, 0
        while i < len(poly1):
            j = 0
            while j < len(poly2):
                if i+j == k:
                    result[i+j] = result[i+j] + (poly1[i] * poly2[j])
                j += 1
            i += 1
    return result



test = [2, 0, 5, 7]
test1 = [3, 4, 2]

print(multiply_polynomials(test, test1))