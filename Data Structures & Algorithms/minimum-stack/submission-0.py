class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        if self.min == None:
            self.min = val
        else:
            self.min = min(self.min, val)
        

    def pop(self) -> None:
        self.min = self.stack[-1][1]
        self.stack = self.stack[:-1]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.min
        
