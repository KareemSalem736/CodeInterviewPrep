# Valid Anagram
# Given two strings s and t, return True if t is an anagram of s, and False otherwise.
# An anagram is a word formed by rearranging the letters of another word.
# Example: "listen" and "silent" are anagrams.

def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {} # [char, frequency]

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True

if __name__ == '__main__':
    print(valid_anagram('string', 'string'))
    print(valid_anagram('notValid', 'noitsnot'))
    print(valid_anagram('listen', 'silent'))
    print(valid_anagram('aab', 'abb'))