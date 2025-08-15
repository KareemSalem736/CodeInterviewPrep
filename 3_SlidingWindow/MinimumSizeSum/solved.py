# Given an array of positive integers nums and an integer target, return the minimal length of a contiguous subarray 
#   [nums[l], ..., nums[r]] whose sum is greater than or equal to target.
# If there is no such subarray, return 0.

def min_subarray_len(target, nums):
    left = 0
    curr_sum = 0
    best = float('inf')

    for right, x in enumerate(nums):
        curr_sum += x

        # shrink from the left while the window is valid
        while curr_sum >= target:
            best = min(best, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return 0 if best == float('inf') else best

if __name__ == '__main__':
    print(min_subarray_len(7, [2,3,1,2,4,3]))   # 2  -> [4,3]
    print(min_subarray_len(4, [1,4,4]))         # 1  -> [4]
    print(min_subarray_len(11, [1,1,1,1,1,1]))  # 0  -> none
    print(min_subarray_len(15, [1,2,3,4,5]))    # 5  -> [1,2,3,4,5]
    print(min_subarray_len(5, [5]))             # 1  -> [5]