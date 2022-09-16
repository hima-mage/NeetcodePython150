class MinStack:
    # init stack to store elements , init minStack to store min element as last one
    def __init__(self):
        self.stack = []
        self.minStack = []
    # add element to stack -> check if val if less that the pop of last element in minStack  append it , or just append the last element again in minStack
    def push(self , val :int):
        self.stack.append(val) # append val in stack
        val = min(val , self.minStack[-1] if self.minStack else val ) # get the min val between current and last element in minStack
        self.minStack.append(val) # append that val in the minStack -> so i can pop it when ask for minElement

    # pop last element from both stack and minStack
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    # get last element of the stack
    def top(self) -> int:
        return  self.stack[-1]

    # get last element of out minStack
    def getMin(self):
        return  self.minStack[-1]









# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()