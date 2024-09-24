# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        result = []
        queue = deque()
        queue.append((0,root))

        while queue:
            curr_level,curr_node = queue.popleft()
            if curr_node:
                queue.append((curr_level+1,curr_node.left))
                queue.append((curr_level+1,curr_node.right))
                res[curr_level].append(curr_node.val)

        for level,val in res.items():
            if level%2 == 0:
                result.append(val)
            elif level%2 == 1:
                result.append(val[::-1])
        return result
