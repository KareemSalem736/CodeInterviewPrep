# Return the index if the target is found. If not, return the index where it should be inserted.

class SI:

if __name__ == "__main__":
    print(SI([1,3,5,6], 5).search_insert())   # 2
    print(SI([1,3,5,6], 2).search_insert())   # 1
    print(SI([1,3,5,6], 7).search_insert())   # 4
    print(SI([1,3,5,6], 0).search_insert())   # 0
