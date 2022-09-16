from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # max Area
        maxArea = 0
        # stack
        stack = []
        # for every element get index and height
        for i, h in enumerate(heights):
            # start will be from this index
            start = i
            # if the last element in stack height > current height so modify the
            while stack and stack[-1][1] > h:
                # get index and height of this element
                index, height = stack.pop()
                # set maxArea to max(oldVal , area of curr and lastelement_in_stack)
                maxArea = max(maxArea, height * (i - index))
                # start is from that index of the last element
                start = index
            # add the start (index) and height of current height
            stack.append((start, h))
        print(stack)
        for i, h in stack:
            print(i, h)
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea


myinput = [2,1,5,6,2,3]
solution = Solution()
solution.largestRectangleArea(myinput)