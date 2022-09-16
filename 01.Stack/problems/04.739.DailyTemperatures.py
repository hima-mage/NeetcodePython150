from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int] ) -> list[int]:
        result = [0] * len(temperatures) # create number of index = len(temperatures)
        stack = [] # pair : [temp , index]
        # i , element
        for i, temperature in enumerate(temperatures):
            # while stack not empty and element > stack[-1][0] = temperature
            while stack and temperature > stack[-1][0]:
                # here i pop last element from stack and destruct it into element , i ->  as it's list
                stackTemperature , stackIndex = stack.pop()
                # here i set result for each element = index of current temp (gt than) - index of the less temp day
                result[stackIndex] = i - stackIndex

            # append list as stack element
            stack.append((temperature, i))
        return  result
