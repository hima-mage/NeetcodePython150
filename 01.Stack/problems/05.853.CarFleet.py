from typing import List


class Solution:
    def carFleet(self, target:int , position: List[int] , speed: List[int]) -> int:
        # pair will be (position , speed) of each car
        pair = [ (p,s) for p, s in zip(position , speed) ]
        # reverse sort the pair list  to get  the first position first
        pair.sort(reverse=True)
        # stack will store the time remain to reach the target destination
        stack = []
        print(pair)
        print(" ")
        for p, s in pair: # reverse sorted Order
            # append the time left to reach the destination -> target
            stack.append((target - p) / s)
            print(stack)
            # if we have more than two time in the stack -> if time of second car < time of prev car -> pop it as they will met eventually and become fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return  len(stack)


solution = Solution()
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

solution.carFleet(target, position, speed)
