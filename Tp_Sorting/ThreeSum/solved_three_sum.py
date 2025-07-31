# Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:
# i != j, j != k, and i != k, and
# nums[i] + nums[j] + nums[k] == 0
# Return the triplets in any order, but no duplicates allowed.

def three_sum(arr):
    if len(arr) < 3:
        return []

    arr.sort()
    results = []

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        j = i + 1
        k = len(arr) - 1

        while j < k:
            total = arr[i] + arr[j] + arr[k]

            if total == 0:
                results.append([arr[i], arr[j], arr[k]])

                while j < k and arr[j] == arr[j + 1]:
                    j += 1
                while j < k and arr[k] == arr[k - 1]:
                    k -= 1

                j += 1
                k -= 1

            elif total < 0:
                j += 1
            else:
                k -= 1

    return results

if __name__ == '__main__':
    print(three_sum([-1, 0, 1, 2, -1, -4]))# Expected: [[-1, -1, 2], [-1, 0, 1]]
    print(three_sum([0, 0, 0, 0]))# Expected: [[0, 0, 0]]
    print(three_sum([-2, 0, 1, 1, 2]))# Expected: [[-2, 1, 1], [-2, 0, 2]]
    print(three_sum([]))# Expected: []
    print(three_sum([0]))# Expected: []
    print(three_sum([0, 1]))# Expected: []
    print(three_sum([-4, -1, -1, 0, 1, 2]))# Expected: [[-1, -1, 2], [-1, 0, 1]]
    print(three_sum([3, -2, 1, 0]))# Expected: [[-2, 1, 1], [-2, 0, 2]] (or variations)
