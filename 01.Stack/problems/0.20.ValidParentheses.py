class Solution:
    def isValid(self, s:str) -> bool:
        # make dictionary to store paranthese as map { key : value }
        map = {")": "(" , "]": "[" , "}": "{"}

        # create stack as empty List
        stack = []

        # loop all char in string
        for c in s:

            # check if the c not in the map -> it's opening parenthese
            if c not in map:
                stack.append(c) # add it to stack -> keep trace the number of opening parethese
                continue

            # check if stack is empty (not stack)  or last element in the stack not in the map keys -> it's opening parenthese
            if not stack or stack[-1] != map[c]:
                return  False # return false -> not valid parenthese

            # it's closing parenthese
            stack.pop()

        return  not stack