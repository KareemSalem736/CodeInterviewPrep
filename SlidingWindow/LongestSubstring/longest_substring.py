# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

def longest_substring(s):
    longest = 0
    left = 0
    set_s = set()

    for right in range(len(s)):
        while s[right] in set_s:
            set_s.remove(s[left])
            left += 1
        longest = max(longest, (right - left) + 1)
        set_s.add(s[right])
    return longest

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
