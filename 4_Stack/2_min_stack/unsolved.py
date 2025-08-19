# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    
class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, num):
        self._stack.append(num)
        if not self._min_stack or self._min_stack[-1] >= num:
            self._min_stack.append(num)
    
    def pop(self):
        if self._stack:
            removed = self._stack.pop()
        if self._min_stack and removed == self._min_stack[-1]:
            self._min_stack.pop()
    
    def top(self):
        return self._stack[-1] if self._stack else None
    
    def get_min(self):
        return self._min_stack[-1] if self._min_stack else None

if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.get_min())  # -3
    stack.pop()
    print(stack.top())      # 0
    print(stack.get_min())  # -2