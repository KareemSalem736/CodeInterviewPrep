# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

class ValidParentheses:
    pass
if __name__ == "__main__":
    examples = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for ex in examples:
        print(ValidParentheses(ex).is_valid())