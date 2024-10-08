# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 중위 순회를 통해 트리의 노드를 리스트에 저장
        nodes = []
        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                nodes.append(node)
                inorder_traversal(node.right)

        # 중위 순회로 노드들을 리스트에 담기
        inorder_traversal(root)
        
        # 잘못된 두 노드 찾기
        first = second = None
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                if not first:
                    first = nodes[i]  # 첫 번째 잘못된 노드
                second = nodes[i + 1]  # 두 번째 잘못된 노드
        
        # 두 노드의 값 교환
        if first and second:
            first.val, second.val = second.val, first.val

                



        