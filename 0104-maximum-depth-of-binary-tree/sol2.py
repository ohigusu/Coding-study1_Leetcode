# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        def depth(node):
            if node is None : return 0
            left_length = depth(node.left)
            right_length = depth(node.right)
            return 1+max(left_length,right_length)
        
        depth_l = 1 + depth(root.left)
        depth_r = 1 + depth(root.right)
        return max(depth_l,depth_r)
