import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = [] # this will be minHeap list , which will be each element [distance , x , y]
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            # for each element calculate the distance then append it to minHeap
            pts.append([dist, x, y])

        res = []
        heapq.heapify(pts) # create heap out from list
        for i in range(k):
            dist, x, y = heapq.heappop(pts) # pump out from heap as it's sorted from the smallest to largest
            res.append([x, y]) # append each point to that result
        return res