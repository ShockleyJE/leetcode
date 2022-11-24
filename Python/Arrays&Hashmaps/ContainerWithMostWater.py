class Solution:
    def maxArea(self, height: List[int]) -> int:
        lptr, rptr = 0, len(height)-1
        lmax, rmax = 0,0
        curr_max_water = 0

        while lptr < rptr:
            # re-evaluate area - min(height[lptr], height[rptr]) * (lptr- rptr)
            curr_max_water = max((min(height[lptr], height[rptr]) * (rptr - lptr)), curr_max_water)
            # if greater than cmw, update cmw

            # shift the lesser pointer
            if height[lptr] < height[rptr]:
                # move left forward
                lptr += 1
                # update lmax
                lmax = min(lmax, height[lptr])
            else:
                # move left forward
                rptr -=1
                # update rmax
                rmax = min(rmax, height[rptr])
        return curr_max_water