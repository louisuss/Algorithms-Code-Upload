import sys


class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def min_dff_bst(self, root):
        if root.left:
            self.min_dff_bst(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.min_dff_bst(root.right)

        return self.result


def min_dff_bst2(self, root):
    prev = -sys.maxsize
    result = sys.maxsize

    stack = []
    node = root

    # 반복 구조 중위 순회 비교 결과
    while stack or node:
        # root 부터 시작해서 왼쪽꺼를 계속 stack 에 넣음
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()

        # 결과최소값 구하기
        result = min(result, node.val-prev)
        # 이전 값을 현재 노드 값으로 변경
        prev = node.val
        # 오른쪽 노드로 이동
        node = node.right

    return result
