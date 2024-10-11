class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        del self.stack[len(self.stack)-1]

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int: 
        output = self.stack[0]
        for i in self.stack:
            if i < output:
                output = i
        
        return output