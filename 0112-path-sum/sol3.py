# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        node_sum_stack = [(root, root.val)]
        has_path = False
        while node_sum_stack:
            node, sum_path = node_sum_stack.pop()
            if not(node.left or node.right):
                has_path = has_path or (sum_path == targetSum)
            if node.left:
                node_sum_stack.append((node.left, sum_path + node.left.val))
            if node.right:
                node_sum_stack.append((node.right, sum_path + node.right.val))
        
        return has_path
