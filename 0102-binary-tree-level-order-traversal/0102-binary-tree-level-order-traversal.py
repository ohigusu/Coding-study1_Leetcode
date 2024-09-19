# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        visit = []
        def level_order(node,l):
            if not node:
                return
            if l >=len(visit):
                visit.append([])

            visit[l].append(node.val)
            level_order(node.left,l+1)
            level_order(node.right,l+1)
        level_order(root,0)
        return visit