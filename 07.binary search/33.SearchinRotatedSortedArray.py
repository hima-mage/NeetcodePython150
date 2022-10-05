"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

binary search keep divide the array  by  2 -> which lead n/2**k -> k = log(n) number of operation
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # loop two ponter means n/2 elements will be searched
        while l <= r:
            # get middle element
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion -> which could be sorted larger than right one
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1