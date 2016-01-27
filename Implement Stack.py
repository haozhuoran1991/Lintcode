class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.items = []
    # @param x, an integer, push a new item into the stack
    # @return nothing
    def push(self, x):
        # Write your code here
        self.items.append(x)
    # @return nothing, pop the top of the stack
    def pop(self):
        # Write your code here
        return self.items.pop()
    # @return an integer, return the top of the stack
    def top(self):
        # Write your code here
        if not self.isEmpty():
            return self.items[len(self.items)-1]
    # @return a boolean, check the stack is empty or not.
    def isEmpty(self):
        # Write your code here
        return len(self.items)==0
