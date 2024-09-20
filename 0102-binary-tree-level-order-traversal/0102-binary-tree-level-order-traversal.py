# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self,root:Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list) 
        queue = deque() 
        queue.append((0,root)) #(level,node)
        while queue:
            curr_level,curr_node = queue.popleft() #선입선출
            if curr_node:
                result[curr_level].append(curr_node.val)
                queue.append((curr_level+1,curr_node.left)) 
                queue.append((curr_level+1,curr_node.right))
                   
        return [val for _,val in result.items()]