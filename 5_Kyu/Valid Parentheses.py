"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""

# My Solution
def valid_parentheses(string):
    parentheses = [elem for elem in string if elem == "(" or elem == ")"]
    counter = 0
    correct = True
    for i in parentheses:
        if i == "(":
            counter += 1
        else:
            counter -= 1
            if counter < 0:
                correct = False
                return correct

    return True if counter == 0 else False

print(valid_parentheses("hi())("))

# Testcase
"""
test.assert_equals(valid_parentheses("hi(hi)()"),True, "should work for 'hi(hi)()'")
test.assert_equals(valid_parentheses("  ("), False, "should work for '  ('")
test.assert_equals(valid_parentheses(")test"), False, "should work for ')test'")
test.assert_equals(valid_parentheses(""), True, "should work for ''")
test.assert_equals(valid_parentheses("hi())("), False, "should work for 'hi())('")
"""

# Better Solution
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False