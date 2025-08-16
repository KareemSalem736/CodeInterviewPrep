# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

class ValidParentheses:
    """Validate a parentheses/brackets string."""

    def __init__(self, s: str) -> None:
        self.s = s

    def is_valid(self) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack: list[str] = []

        for ch in self.s:
            if ch in pairs.values():  # left bracket
                stack.append(ch)
            elif ch in pairs:  # right bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                return False

        return not stack


if __name__ == "__main__":
    examples = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for ex in examples:
        print(ValidParentheses(ex).is_valid())
