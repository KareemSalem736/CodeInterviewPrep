# Given a sorted array of integers nums and an integer target, return the index of target if it exists, otherwise -1.

class BS:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def binary_search(self):
        right = len(self.nums) - 1
        left = 0

        while left <= right:
            middle = (left + right) // 2
            if self.nums[middle] == self.target:
                return middle
            elif self.nums[middle] > self.target:
                right = middle - 1
            elif self.nums[middle] < self.target:
                left = middle + 1
        return -1

if __name__ == "__main__":
    print(BS([-1,0,3,5,9,12], 9).binary_search())   # 4
    print(BS([-1,0,3,5,9,12], 2).binary_search())   # -1
    