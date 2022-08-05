# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # base case, assuming we made it down all the way for a given node
        if not p and not q:
            return True
        
        # Next case, both 
        elif p and q:
            # equivalent, traverse left and right
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        # Otherwise, one but not the other- not identical
        else:
            return False