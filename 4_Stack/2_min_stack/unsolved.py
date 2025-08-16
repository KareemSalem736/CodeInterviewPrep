# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    

if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.get_min())  # -3
    stack.pop()
    print(stack.top())      # 0
    print(stack.get_min())  # -2