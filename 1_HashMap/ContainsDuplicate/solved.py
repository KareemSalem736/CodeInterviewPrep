# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice, or false if every element is distinct.

def contains_duplicate(nums):
    seen = {}

    for i in range(len(nums)):
        num = nums[i]
        if num in seen:
            return True
        seen[num] = True
    return False

if __name__ == '__main__':
    print(contains_duplicate([1, 2, 3, 4, 5, 6, 7]))
    print(contains_duplicate([1, 4, 6, 6, 7, 7]))
