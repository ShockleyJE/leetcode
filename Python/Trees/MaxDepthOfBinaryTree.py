# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def find_depth(node: TreeNode, depth: int):
            # base case
            if node.left and node.right == None:
                return depth

            l_depth = find_depth(node.left, depth + 1) if node.left else depth
            r_depth = find_depth(node.right, depth + 1) if node.right else depth

            return max(l_depth, r_depth)
        
        return find_depth(root, 1)


# RECURSIVE DFS
#class Solution:
#    def maxDepth(self, root: TreeNode) -> int:
#        if not root:
#            return 0
#
#        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))