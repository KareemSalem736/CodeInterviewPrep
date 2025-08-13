# Given an array of positive integers nums and an integer target, return the minimal length of a contiguous subarray [nums[l], ..., nums[r]] whose sum is greater than or equal to target.
# If there is no such subarray, return 0.

def min_size_sum(nums, target):
    nums_sum = 0
    left = 0
    
    for right, chr in enumerate(nums):
        if chr
    return nums_sum

if __name__ == '__main__':
    print(min_size_sum([2,3,1,2,4,3], 7))
