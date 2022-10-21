#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a set out of the nums
        # allow us to look up each num in constant time
        hash_tbl = dict()
        for i,n in enumerate(nums):
            # before adding to the map, 
            # check if we have entered the target value already
            t = target - n
            if t in hash_tbl:
                return [i, hash_tbl[t]]

            hash_tbl[n] = i