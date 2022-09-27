# library to operate over the heap
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # convert each element into  negative value
        heapq.heapify(stones) # create heap out from the list

        while len(stones) > 1:
            # pop last element -> which be the largest values -> so on
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # if this there is diff -> smash them and then put them into the heap
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])