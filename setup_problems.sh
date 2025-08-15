#!/bin/bash

# Helper function to make problem dirs and files with boilerplate
make_problem() {
    section_dir="$1"
    problem_dir="$2"
    problem_text="$3"
    test_prints="$4"

    mkdir -p "$section_dir/$problem_dir"
    for file in solved.py unsolved.py; do
        cat > "$section_dir/$problem_dir/$file" <<EOF
\"\"\"$problem_text\"\"\"

def ${problem_dir// /_}():
    pass

if __name__ == "__main__":
$test_prints
EOF
    done
}

# ----------------------
# 4) Stack
# ----------------------
make_problem "4_stack" "valid_parentheses" \
"Valid Parentheses (LeetCode 20)
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid." \
"    print(valid_parentheses(\"()\"))        # True
    print(valid_parentheses(\"()[]{}\"))    # True
    print(valid_parentheses(\"(]\"))        # False
    print(valid_parentheses(\"([)]\"))      # False
    print(valid_parentheses(\"{[]}\"))      # True"

make_problem "4_stack" "min_stack" \
"Min Stack (LeetCode 155)
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time." \
"    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin())   # -3
    stack.pop()
    print(stack.top())      # 0
    print(stack.getMin())   # -2"

make_problem "4_stack" "daily_temperatures" \
"Daily Temperatures (LeetCode 739)
Given a list of daily temperatures, return a list that tells for each day how many days until a warmer temperature." \
"    print(daily_temperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
    print(daily_temperatures([30,40,50,60]))               # [1,1,1,0]
    print(daily_temperatures([30,60,90]))                  # [1,1,0]"

# ----------------------
# 5) Binary Search
# ----------------------
make_problem "5_binary_search" "binary_search" \
"Binary Search (LeetCode 704)
Given a sorted array of integers nums and an integer target, return the index of target if it exists, otherwise -1." \
"    print(binary_search([-1,0,3,5,9,12], 9))   # 4
    print(binary_search([-1,0,3,5,9,12], 2))   # -1"

make_problem "5_binary_search" "search_insert_position" \
"Search Insert Position (LeetCode 35)
Return the index if the target is found. If not, return the index where it should be inserted." \
"    print(search_insert([1,3,5,6], 5))   # 2
    print(search_insert([1,3,5,6], 2))   # 1
    print(search_insert([1,3,5,6], 7))   # 4
    print(search_insert([1,3,5,6], 0))   # 0"

make_problem "5_binary_search" "find_min_in_rotated_sorted_array" \
"Find Minimum in Rotated Sorted Array (LeetCode 153)
Find the minimum element in a rotated sorted array." \
"    print(find_min([3,4,5,1,2]))         # 1
    print(find_min([4,5,6,7,0,1,2]))     # 0
    print(find_min([11,13,15,17]))       # 11"

# ----------------------
# 6) Heap
# ----------------------
make_problem "6_heap" "kth_largest_element" \
"Kth Largest Element in an Array (LeetCode 215)
Find the kth largest element in an unsorted array." \
"    print(kth_largest([3,2,1,5,6,4], 2))         # 5
    print(kth_largest([3,2,3,1,2,4,5,5,6], 4))   # 4"

make_problem "6_heap" "top_k_frequent_elements" \
"Top K Frequent Elements (LeetCode 347)
Return the k most frequent elements." \
"    print(top_k_frequent([1,1,1,2,2,3], 2))   # [1,2]
    print(top_k_frequent([1], 1))             # [1]"

make_problem "6_heap" "last_stone_weight" \
"Last Stone Weight (LeetCode 1046)
Simulate smashing two heaviest stones until none or one remains." \
"    print(last_stone_weight([2,7,4,1,8,1]))   # 1
    print(last_stone_weight([1]))             # 1"

# ----------------------
# 7) Backtracking
# ----------------------
make_problem "7_backtracking" "subsets" \
"Subsets (LeetCode 78)
Return all possible subsets (the power set) of a list of unique integers." \
"    print(subsets([1,2,3]))  # [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]"

make_problem "7_backtracking" "permutations" \
"Permutations (LeetCode 46)
Return all permutations of a list of distinct integers." \
"    print(permute([1,2,3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]"

make_problem "7_backtracking" "combination_sum" \
"Combination Sum (LeetCode 39)
Return all unique combinations of candidates where chosen numbers sum to target. Unlimited use of each candidate allowed." \
"    print(combination_sum([2,3,6,7], 7))  # [[2,2,3],[7]]
    print(combination_sum([2,3,5], 8))    # [[2,2,2,2],[2,3,3],[3,5]]"

# ----------------------
# 8) Dynamic Programming
# ----------------------
make_problem "8_dynamic_programming" "climbing_stairs" \
"Climbing Stairs (LeetCode 70)
Return the number of distinct ways to climb to the top with steps of 1 or 2." \
"    print(climb_stairs(2))   # 2
    print(climb_stairs(3))   # 3"

make_problem "8_dynamic_programming" "house_robber" \
"House Robber (LeetCode 198)
Return the maximum money you can rob without robbing adjacent houses." \
"    print(house_robber([1,2,3,1]))   # 4
    print(house_robber([2,7,9,3,1])) # 12"

make_problem "8_dynamic_programming" "coin_change" \
"Coin Change (LeetCode 322)
Return the fewest coins needed to make up the given amount, or -1 if impossible." \
"    print(coin_change([1,2,5], 11))   # 3
    print(coin_change([2], 3))        # -1
    print(coin_change([1], 0))        # 0"