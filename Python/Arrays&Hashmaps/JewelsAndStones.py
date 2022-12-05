#https://leetcode.com/problems/jewels-and-stones/submissions/855803763/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 
        j_set = set(jewels)
        strikes = 0
        for s in stones:
            if s in j_set:
                strikes += 1
    
        return strikes