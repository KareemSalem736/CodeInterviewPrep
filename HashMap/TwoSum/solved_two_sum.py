# Prompt: Two Sum
# Given an array of integers 'nums' and an integer 'target', return the two numbers such that they add up to 'target'.
# You may assume that each input has exactly one solution, and you may not use the same element twice.

# Approach - Hashmap
# Goal: For each number, check if there's another number that equals 'target - num'
# Hashmap idea: Store each number's index in a dictionary as you loop
# If the complement is in the map, 'target - num', return the two indices


def two_sums(nums, target):
    seen = {}

    for i in range(len(nums)):
        num = nums[i]
        helper = target - num

        if helper in seen:
            return [seen[helper], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    print(two_sums([5, 4, 6, 9], 10))
    print(two_sums([2, 7, 11, 15], 9))
    print(two_sums([1, 2, 3, 4, 5, 6], 7))
