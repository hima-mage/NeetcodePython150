from typing import List

"""
    if it's operand add to stack -> keep going 
    if u met operator get last two element made operation on them then append them to stack so the evaluation of the experssion could be used 
        with next operand
    so this means the stack will remain with the only value of this operation as alaways will be operand in last of the RPN 
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens :
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c =="-":
                a, b = stack.pop() , stack.pop()
                stack.append(b - a)

            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]