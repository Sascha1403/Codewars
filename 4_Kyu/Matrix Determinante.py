"""
Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

A 1x1 matrix |a| has determinant a.

A 2x2 matrix [ [a, b], [c, d] ] or

|a  b|
|c  d|

has determinant: a*d - b*c.

The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants
of n matrices ofn-1 x n-1 size.

For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or

|a b c|
|d e f|
|g h i|

the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) refers to taking the
determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs:

|- - -|
|- e f|
|- h i|

Note the alternation of signs.

The determinant of larger matrices are calculated analogously, e.g.
if M is a 4x4 matrix with first row [a, b, c, d], then:

det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)

Testcase
m1 = [ [1, 3], [2,5]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]

test.assert_equals(determinant([[1]]), 1, "Determinant of a 1 x 1 matrix yields the value of the one element")
test.assert_equals(determinant(m1), -1, "Should return 1 * 5 - 3 * 2, i.e., -1 ")
test.expect(determinant(m2) == -20)
"""
import numpy as np
import copy


def determinant(matrix):
    result = 0
    l = len(matrix)

    # base Case when lenght of matrix is 1
    if l == 1:
        return matrix[0][0]

    # base Case when lenght of matrix is 2
    if l == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # if lenght of matrix > 2
    for i in range(l):
        sub_matrix = [(row[0:i] + row[i + 1:]) for row in matrix[1:]]
        if i % 2 == 0:
            result += matrix[0][i] * determinant(sub_matrix)
        else:
            result -= matrix[0][i] * determinant(sub_matrix)

    return result


m2 = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]
print(determinant(m2))

### Better Solution
def determinant(m):
    if len(m) == 2 : return (m[0][0]*m[1][1]) - (m[0][1]*m[1][0])
    li = [[m[j][:i] + m[j][i+1:] for j in range(1,len(m))] for i in range(len(m))]
    return sum(-m[0][i]*(determinant(j)) if i&1 else m[0][i]*(determinant(j)) for i,j in enumerate(li))

