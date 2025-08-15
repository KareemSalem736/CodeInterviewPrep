# You are given a string s consisting of only uppercase English letters and an integer k.
# You can replace at most k characters in the string so that the resulting substring contains only the same character.
# Return the length of the longest such substring.

def char_replace(s, k):
    counts = {}
    left = 0
    max_count = 0
    best = 0

    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        max_count = max(max_count, counts[ch])

        while (right - left + 1) - max_count > k:
            left_ch = s[left]
            counts[left_ch] -= 1
            left += 1
        best = max(best, right - left + 1)

    return best

if __name__ == '__main__':
    print(char_replace("ABAB", 2))        # Expected: 4
    print(char_replace("AABABBA", 1))     # Expected: 4
    print(char_replace("ABCDE", 1))       # Expected: 2
    print(char_replace("AAAA", 2))        # Expected: 4
    print(char_replace("BAAA", 0))        # Expected: 3
    print(char_replace("BAAAAB", 2))      # Expected: 6
    print(char_replace("ABBB", 2))        # Expected: 4