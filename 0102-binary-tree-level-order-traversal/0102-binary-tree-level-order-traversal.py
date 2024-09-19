# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)
        queue =deque()        
        queue.append((0,root))
        while queue:
            curr_level,curr_node = queue.popleft()
            if curr_node:
                queue.append((curr_level+1,curr_node.left))
                queue.append((curr_level+1,curr_node.right))
                result[curr_level].append(curr_node.val)
        return [v for key,v in result.items()]