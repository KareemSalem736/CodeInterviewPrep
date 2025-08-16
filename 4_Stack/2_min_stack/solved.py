# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack:
    """Stack that supports push, pop, top and retrieving min"""

    def __init__(self) -> None:
        self._stack: list[int] = []
        self._min_stack: list[int] = []
    
    def push(self, val) -> None:
        self._stack.append(val)
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)
    
    def pop(self) -> None:
        if self._stack: 
            val = self._stack.pop()
            if val == self._min_stack[-1]:
                self._min_stack.pop()

    def top(self) -> int:
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