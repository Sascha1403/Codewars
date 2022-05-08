"""
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution('XXI') # should return 21

Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

test.describe("Example Tests")
test.assert_equals(solution('XXI'), 21, 'XXI should == 21')
test.assert_equals(solution('I'), 1, 'I should == 1')
test.assert_equals(solution('IV'), 4, 'IV should == 4')
test.assert_equals(solution('MMVIII'), 2008, 'MMVIII should == 2008')
test.assert_equals(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666')
"""
dic = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def solution(roman):
    num = [dic[elem] for elem in roman]
    chache = [elem if elem >= max(num[index:]) else (elem * -1) for index, elem in enumerate(num)]
    return sum(chache)

print(solution('IV'))