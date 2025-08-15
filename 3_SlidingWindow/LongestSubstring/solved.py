# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

def longest_substring(s):
    char_set = set()
    max_len = 0
    left = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

if __name__ == '__main__':
    print(longest_substring("abcabcbb"))   # Expected: 3  → "abc"
    print(longest_substring("bbbbb"))      # Expected: 1  → "b"
    print(longest_substring("pwwkew"))     # Expected: 3  → "wke"
    print(longest_substring(""))           # Expected: 0
    print(longest_substring(" "))          # Expected: 1
    print(longest_substring("au"))         # Expected: 2  → "au"
    print(longest_substring("dvdf"))       # Expected: 3  → "vdf"
    print(longest_substring("abba"))       # Expected: 2  → "ab" or "ba"
    print(longest_substring("abcdeafgh"))  # Expected: 8  → "bcdeafgh"
    print(longest_substring("a" * 10000))  # Expected: 1
