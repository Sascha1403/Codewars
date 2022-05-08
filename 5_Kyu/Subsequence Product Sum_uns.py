"""
Given an array of integers and an integer m, return the sum of the product of its subsequences of length m.

Ex1:

a = [1, 2, 3]
m = 2

the subsequences (of length 2) are (1,2) (1,3) (2,3), you should multiply the numbers of each subsequence and take their sum

product_sum = (1*2) + (1*3) + (2*3) #=> 11

Ex2:

a = [2,3,4,5]
m = 3

the subsequences (of length 3) are (2,3,4) (2,4,5) (2,3,5) (3,4,5)

product_sum = (2*3*4) + (2*3*5) + (2*4*5) + (3*4*5) #=> 154

Task:

Write a function `product_sum(a, m)`` that does as described above

The sum can be really large, so return the result in modulo 109+7
Constraints

0 <= A[i] < 1000000

1 <= m <= 20
49 random tests |A| <= 10^4
1 big test |A| = 10^5

m < |A|

# Tests
tc = [
    ([2,3, 4, 5],3, 154 ),
    ([1, 2, 3], 2, 11),
    ([5, 7, 2, 3], 3, 247),
    ([3,10,7,9,1,4,5,2,8,6], 7, 8409500),
    ([10,7,8,5,6,9,4,1,2,3], 8, 12753576),
    ([1,7,6,10,21,5,9,8,5,4], 2, 2469),
    ([6,7,8,5,2,4,9,3,1,10], 6, 3416930),
    ([3,2,9,1,7,10,5,6,8,4], 4, 157773),
    ([9,8,10,4,2,7,5,1,3,6], 3, 18150),
    ([3,3,1,7,6,8,1,4,6,10], 4, 94837),
    ([6,8,1,7,2,10,5,9,3,4], 5, 902055),
    ([10,3,4,9,5,8,6,7,1,2], 1, 55),
    ([7,9,4,2,3,10,8,6,5,1], 9, 10628640)
]

test.it("Sample tests")
for arr, m, res in tc:
    test.assert_equals(product_sum(arr,m), res, 'Wrong Value')


Test ([1,7,6,10,21,5,9,8,5,4], 2, 2469),

a = [1,7,6,10,21,5,9,8,5,4]
 
subset = [[a[i],a [j]] for i in range(len(a)) for j in range(i+1, len(a))]
test = [math.prod(subset[i]) for i in range(len(subset))]
res = sum(test)

"""

import math


def product_sum(a, m):
    # Rekursionsanker bestimmen
    if (len(a) == m):
        return math.prod(a)

print(product_sum([1, 2, 3, 4], 2))

