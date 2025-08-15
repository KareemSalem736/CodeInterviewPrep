# Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.
# An input string is valid if:
# 	1.	Open brackets are closed by the same type of brackets.
# 	2.	Open brackets are closed in the correct order.

def valid_parentheses(s):
    return

if __name__ == '__main__':
    print(valid_parentheses("()"))        # True
    print(valid_parentheses("()[]{}"))    # True
    print(valid_parentheses("(]"))        # False
    print(valid_parentheses("([)]"))      # False
    print(valid_parentheses("{[]}"))      # True