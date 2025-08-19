# Return the index if the target is found. If not, return the index where it should be inserted.

class SI:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        
    def search_insert(self):
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
        return left

if __name__ == "__main__":
    print(SI([1,3,5,6], 5).search_insert())   # 2
    print(SI([1,3,5,6], 2).search_insert())   # 1
    print(SI([1,3,5,6], 7).search_insert())   # 4
    print(SI([1,3,5,6], 0).search_insert())   # 0
