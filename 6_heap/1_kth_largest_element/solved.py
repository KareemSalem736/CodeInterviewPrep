# Find the kth largest element in an unsorted array.
class K:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def kth_largest(self):
        

if __name__ == "__main__":
    print(K([3,2,1,5,6,4], 2).kth_largest())         # 5
    print(K([3,2,3,1,2,4,5,5,6], 4).kth_largest())   # 4
