"""
Write a rotate function that rotates a two-dimensional array (a matrix) either clockwise or anti-clockwise by 90 degrees, and returns the rotated array.

The function accepts two parameters: an array, and a string specifying the direction or rotation. The direction will be either "clockwise" or "counter-clockwise".

Here is an example of how your function will be used:

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate(matrix, "clockwise") #  Would return  [[7, 4, 1], [8, 5, 2],  [9, 6, 3]]

To help you visualize the rotated matrix, here it is formatted as a grid:

 [[7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]]

Rotated counter-clockwise it would looks like this:

 [[3, 6, 9],
  [2, 5, 8],
  [1, 4, 7]]

#### Test Description ###

@test.describe("Example Tests")
def test_group():
    @test.it("Test a matrix with equal numbers of rows/cols")
    def test_case():
        matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]

        test.assert_equals(rotate(matrix, 'counter-clockwise'), [[3,6,9],[2,5,8],[1,4,7]])
        test.assert_equals(rotate(matrix, 'clockwise'), [[7,4,1],[8,5,2],[9,6,3]])
        test.assert_equals(rotate(rotate(matrix, 'counter-clockwise'), 'clockwise'), [[1,2,3],[4,5,6],[7,8,9]])
        test.assert_equals(rotate(rotate(rotate(rotate(matrix, 'clockwise'), 'clockwise'), 'clockwise'), 'clockwise'), [[1,2,3],[4,5,6],[7,8,9]])

    @test.it("Test a matrix with unequal number of rows/cols")
    def test_case():
        matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9],
                  [10,11,12]]

        test.assert_equals(rotate(matrix, 'counter-clockwise'), [[3,6,9,12],[2,5,8,11],[1,4,7,10]])
        test.assert_equals(rotate(matrix, 'clockwise'), [[10,7,4,1],[11,8,5,2],[12,9,6,3]])

    @test.it("Test a matrix with only one row/col")
    def test_case():
        matrix = [[1,2,3]]

        test.assert_equals(rotate(matrix, 'counter-clockwise'), [[3],[2],[1]])
        test.assert_equals(rotate(matrix, 'clockwise'), [[1],[2],[3]])
        test.assert_equals(rotate(rotate(matrix, 'clockwise'), 'clockwise'), [[3,2,1]])

    @test.it("Test a single cell matrix")
    def test_case():
        matrix = [[1]]

        test.assert_equals(rotate(matrix, 'counter-clockwise'), [[1]])
"""


def rotate(matrix, direction):
    newMatrix = [None] * len(matrix[0])
    i = 0
    while i < len(matrix[0]):
        newMatrix[i] = [vector[i] for vector in matrix]
        i += 1


    if direction == 'clockwise':
        return [vector[::-1] for vector in newMatrix]
    else:
        return newMatrix[::-1]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

print(rotate(matrix, 'counter-clockwise'))
print(rotate(matrix, 'clockwise'))

matrix1 = [[1,2,3]]

print(rotate(matrix1, 'counter-clockwise'))
print(rotate(matrix1, 'clockwise'))

"""
 test.assert_equals(rotate(matrix, 'counter-clockwise'), [[3,6,9,12],[2,5,8,11],[1,4,7,10]])
 test.assert_equals(rotate(matrix, 'clockwise'), [[10,7,4,1],[11,8,5,2],[12,9,6,3]])
 
  matrix = [[1,2,3]]

        test.assert_equals(rotate(matrix, 'counter-clockwise'), [[3],[2],[1]])
        test.assert_equals(rotate(matrix, 'clockwise'), [[1],[2],[3]])
        test.assert_equals(rotate(rotate(matrix, 'clockwise'), 'clockwise'), [[3,2,1]])
"""

### Better Solution
import numpy as np
d = {"clockwise" : -1, "counter-clockwise" : 1}

def rotate(matrix, direction):
    return np.rot90(matrix, d[direction]).tolist()

print("\nBetter Solution")
print(rotate(matrix, 'counter-clockwise'))
print(rotate(matrix, 'clockwise'))

print(rotate(matrix1, 'counter-clockwise'))
print(rotate(matrix1, 'clockwise'))