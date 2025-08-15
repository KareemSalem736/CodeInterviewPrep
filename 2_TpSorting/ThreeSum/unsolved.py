# Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:
# i != j, j != k, and i != k, and
# nums[i] + nums[j] + nums[k] == 0
# Return the triplets in any order, but no duplicates allowed.

def three_sum(arr):

    return 

if __name__ == '__main__':
    print(three_sum([]))# Expected: []
    print(three_sum([0]))# Expected: []
    print(three_sum([0, 1]))# Expected: []
    print(three_sum([3, -2, 1, 0]))# Expected: []
    print(three_sum([-4, -1, -1, 0, 1, 2]))# Expected: [[-1, -1, 2], [-1, 0, 1]]
    print(three_sum([-2, 0, 1, 1, 2]))# Expected: [[-2, 1, 1], [-2, 0, 2]]
    print(three_sum([0, 0, 0, 0]))# Expected: [[0, 0, 0]]
    print(three_sum([-1, 0, 1, 2, -1, -4]))# Expected: [[-1, -1, 2], [-1, 0, 1]]
