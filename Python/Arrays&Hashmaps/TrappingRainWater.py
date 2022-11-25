class Solution:
    def trap(self, height: List[int]) -> int:
        """
        4
        3                       X
        2           X   -   -   X
        1   X   -   X   X   X   X
      

        6
        5                       X 
        4   X                   X
        3   X           X       X
        2   X   X       X   X   X
        1   X   X       X   X   X

        """

        if not height: return 0

        lptr,rptr = 0, len(height)-1
        lmax, rmax = height[lptr], height[rptr]
        accum = 0

        # iterate over the array
        # on each tick
            # move the pointer of the lesser max
            # reevaluate the lesser max
            # add the difference of the local max & current position to the accumulated water
        while lptr < rptr:
            if lmax < rmax:
                lptr += 1
                lmax = max(height[lptr], lmax)
                accum += lmax - height[lptr]
            else:
                rptr -= 1
                rmax = max(height[rptr], rmax)
                accum += rmax - height[rptr]

        return accum
        