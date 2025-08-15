# Valid Palindrome
#  A phrase is a palindrome if, after converting all uppercase letters into lowercase and removing all non-alphanumeric characters, it reads the same forward and backward.
# Return True if it is a palindrome, and False otherwise.

def valid_palindrome(s):
    return
if __name__ == '__main__':
    print(valid_palindrome("A man, a plan, a canal: Panama"))  # True
    print(valid_palindrome("race a car"))                      # False
    print(valid_palindrome("madam"))                           # True
    print(valid_palindrome("no lemon, no melon"))              # True
    print(valid_palindrome("Was it a car or a cat I saw?"))    # True

    print(valid_palindrome(""))                # True (empty string is a palindrome)
    print(valid_palindrome("a"))               # True (single char)
    print(valid_palindrome("aa"))              # True
    print(valid_palindrome("ab"))              # False

    print(valid_palindrome("12321"))           # True (numbers only)
    print(valid_palindrome("123@321"))         # True (ignores @)
    print(valid_palindrome("1a2"))             # False
    print(valid_palindrome("1a1"))             # True
