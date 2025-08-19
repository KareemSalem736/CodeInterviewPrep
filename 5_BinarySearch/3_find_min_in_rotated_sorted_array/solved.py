# Find the minimum element in a rotated sorted array.

class Min:
    def __init__(self, nums):
        self.nums = nums
    def find_min(self):
        left = 0
        right = len(self.nums) - 1
        
        while left < right:
            middle = (left + right) // 2
            if self.nums[middle] > self.nums[right]:
                left = middle + 1
            else:
                right = middle
        return self.nums[left]

if __name__ == "__main__":
    print(Min([3,4,5,1,2]).find_min())         # 1
    print(Min([4,5,6,7,0,1,2]).find_min())     # 0
    print(Min([11,13,15,17]).find_min())       # 11
