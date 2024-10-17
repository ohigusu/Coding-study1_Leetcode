# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        def traverse(root,currSum):
            if not root.left and not root.right:
                return currSum == targetSum
            if root.left and traverse(root.left,currSum+root.left.val):
                return True
            if root.right and traverse(root.right,currSum+root.right.val):
                return True
            return False
        return traverse(root,root.val)
                    
                
