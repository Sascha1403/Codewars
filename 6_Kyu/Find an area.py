"""
You have an array or list of coordinates or points (e.g. [ [1, 1], [3, 4], ... , [5, 2] ]), and your task is to find the area under the graph defined by these points (limited by x of the first and last coordinates as left and right borders, y = 0 as the bottom border and the graph as top border).

Notes:

    x can be negative;
    x of the next pair of coordinates will always be greater then previous one;
    y >= 0;
    the array will contain more than 2 coordinates.

test.assert_equals(find_area([Point(0,0), Point(1,4), Point(3,2)]), 8)
test.assert_equals(find_area([Point(-3, 0), Point(-1, 4), Point(3, 2)]), 16)
test.assert_equals(find_area([Point(-3, 2), Point(-1, 0), Point(3, 2)]), 6)
test.assert_equals(find_area([Point(-3, 2), Point(3, 5)]), 21)
test.assert_equals(find_area([Point(-3, 2), Point(-1, 5), Point(0, 3), Point(3, 7), Point(4, 6)]), 32.5)
"""
class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

def find_area(points):
    xpoint = [pos.X for pos in points]
    ypoint = [pos.Y for pos in points]
    xdiff = [abs(xpoint[i] - xpoint[i + 1]) for i in range(len(points) - 1)]
    ydiff = [abs(ypoint[i] - ypoint[i + 1]) for i in range(len(points) - 1)]
    ymin = [min(ypoint[i], ypoint[i + 1]) for i in range(len(points) - 1)]
    partArea = [1/2 * ydiff[i] * xdiff[i] + xdiff[i] * ymin[i] for i in range(len(points) - 1)]
    SumArea = sum(partArea)
    return SumArea

print(find_area([Point(0,0), Point(1,4), Point(3,2)]))

### Better Solution
def find_area(points):
    return sum((p2.X - p1.X) * (p1.Y + p2.Y) / 2 for p1, p2 in zip(points, points[1:]))

