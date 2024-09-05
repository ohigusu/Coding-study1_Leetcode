# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        def dfs(visited, curr):
            if curr is None:
                return
            visited.append(str(curr.val))
            if curr.left is None and curr.right is None:  # 리프 노드일 때
                answer.append("->".join(visited))  # 경로를 결과에 추가
            else:
                dfs(visited, curr.left)  # 왼쪽 자식 탐색
                dfs(visited, curr.right)  # 오른쪽 자식 탐색
                visited.pop()  # 백트래킹을 위해 마지막 노드를 제거

        dfs([], root)
        return answer
