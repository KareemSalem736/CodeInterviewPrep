# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

def valid_parentheses(s):
    pass

if __name__ == "__main__":
    print(valid_parentheses("()"))        # True
    print(valid_parentheses("()[]{}"))    # True
    print(valid_parentheses("(]"))        # False
    print(valid_parentheses("([)]"))      # False
    print(valid_parentheses("{[]}"))      # True
