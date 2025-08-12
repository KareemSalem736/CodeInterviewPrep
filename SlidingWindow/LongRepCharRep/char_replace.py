# You are given a string s consisting of only uppercase English letters and an integer k.
# You can replace at most k characters in the string so that the resulting substring contains only the same character.
# Return the length of the longest such substring.

def char_replace(s, k):
    char_count = {}
    longest = 0

    for char in s:
        char_count[char] += 1
    for value in char_count:
        longest = value if k <= value else value - k

    return longest

if __name__ == '__main__':
    print(char_replace("ABAB", 2))        # Expected: 4
    print(char_replace("AABABBA", 1))     # Expected: 4
    print(char_replace("ABCDE", 1))       # Expected: 2
    print(char_replace("AAAA", 2))        # Expected: 4
    print(char_replace("BAAA", 0))        # Expected: 3
    print(char_replace("BAAAAB", 2))      # Expected: 6
    print(char_replace("ABBB", 2))        # Expected: 4