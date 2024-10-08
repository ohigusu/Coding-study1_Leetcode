class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        # 교환된 두 노드를 저장할 변수 초기화
        first = second = prev = None

        # 중위 순회 함수 정의
        def inorder_traversal(node: TreeNode):
            nonlocal first, second, prev
            if not node:
                return

            # 왼쪽 서브트리 순회
            inorder_traversal(node.left)

            # 순서가 어긋난 노드 탐지
            if prev and prev.val > node.val:
                if not first:
                    first = prev  # 첫 번째 어긋난 노드
                second = node  # 두 번째 어긋난 노드

            # 이전 노드 업데이트
            prev = node

            # 오른쪽 서브트리 순회
            inorder_traversal(node.right)

        # 중위 순회를 통해 교환된 두 노드 찾기
        inorder_traversal(root)

        # 두 노드의 값을 교환하여 트리 복구
        if first and second:
            first.val, second.val = second.val, first.val
