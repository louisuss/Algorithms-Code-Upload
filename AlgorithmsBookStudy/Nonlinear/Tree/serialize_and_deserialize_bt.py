from collections import deque


def serialize(root):
    q = deque([root])
    result = ['#']

    while q:
        node = q.popleft()
        if node:
            q.append(node.left)
            q.append(node.right)

            result.append(str(node.val))
        else:
            result.append('#')
    return ''.join(result)


def deserialize(data):
    # 예외처리
    if data == '# #':
        return None

    nodes = data.split()

    root = TreeNode(int(nodes[1]))
    q = deque([root])
    index = 2

    # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
    while q:
        node = q.popleft()
        if nodes[index] is not '#':
            node.left = TreeNode(int(nodes[index]))
            q.append(node.left)
        index += 1

        if nodes[index] is not '#':
            node.right = TreeNode(int(nodes[index]))
            q.append(node.right)
        index += 1
    return root
