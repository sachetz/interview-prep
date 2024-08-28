from collections import deque

class SpecialStack:
    def __init__(self):
        self.stk = deque()
        self.minVal = None

    def push(self, data):
        if not self.stk:
            self.stk.append(data)
            self.minVal = data
        elif data < self.minVal:
            self.stk.append(2 * data - self.minVal)
            self.minVal = data
        else:
            self.stk.append(data)

    def pop(self):
        if self.stk:
            curr = self.stk.pop()
            if curr <= self.minVal:
                self.minVal = 2 * self.minVal - curr
        
    def top(self):
        if not self.stk:
            return -1
        
        curr = self.stk[-1]
        if curr < self.minVal:
            return self.minVal
        else:
            return curr
        
    def get_min(self):
        if not self.stk:
            return -1
        return self.minVal