from collections import deque

# pythonic-way


def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root


# 반복 구조로 BFS
def invert_tree2(root):
    q = deque([root])

    while q:
        node = q.popleft()
        # 부모 노드부터 하향식 스왑
        node.left, node.right = node.right, node.left

        q.append(node.left)
        q.append(node.right)
    return root

# 반복 구조로 DFS


def invert_tree3(root):
    stack = deque([root])

    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        stack.append(node.left)
        stack.append(node.right)
    return root

# 반복 구조로 DFS 후위순회


def invert_tree4(root):
    stack = deque([root])

    while stack:
        node = stack.pop()

        if node:
            stack.append(node.left)
            stack.append(node.right)

            node.left, node.right = node.right, node.left  # 후위 순회
        return root
