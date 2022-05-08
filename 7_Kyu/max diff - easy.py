"""
You must implement a function that returns the difference between the largest and the smallest value in a given list / array (lst) received as the parameter.

    lst contains integers, that means it may contain some negative numbers
    if lst is empty or contains a single element, return 0
    lst is not sorted

[1, 2, 3, 4]   //  returns 3 because 4 -   1  == 3
[1, 2, 3, -4]  //  returns 7 because 3 - (-4) == 7

Have fun!

TestCases

import codewars_test as test
from solution import max_diff

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(max_diff([0, 1, 2, 3, 4, 5, 6]), 6);
        test.assert_equals(max_diff([-0, 1, 2, -3, 4, 5, -6]), 11);
        test.assert_equals(max_diff([0, 1, 2, 3, 4, 5, 16]), 16);
        test.assert_equals(max_diff([16]), 0);
        test.assert_equals(max_diff([]), 0);
"""

def max_diff(list):
    if not list: return 0
    return max(list) - min(list)

print(max_diff([-0, 1, 2, -3, 4, 5, -6]))