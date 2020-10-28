# DFS BF 검색
def range_sum_bst(root, l, r):
    if not root:
        return 0

    return (root.val if l <= root.val <= r else 0) + range_sum_bst(root.left, l, r) + range_sum_bst(root.right, l, r)

# DFS 가지치기로 필요한 노드만 검색


def range_sum_bst2(root, l, r):
    def dfs(node):
        if not node:
            return 0

        if node.val < l:
            return dfs(node.right)
        elif node.val > r:
            return dfs(node.left)
        return node.val + dfs(node.left) + dfs(node.right)

    return dfs(root)

# 반복 구조 DFS


def range_sum_bst3(root, l, r):
    stack, sum = [root], 0
    # 스택 이용 필요한 노드 DFS 반복
    while stack:
        node = stack.pop()
        if node:
            if node.val > l:
                stack.append(node.left)
            elif node.val < r:
                stack.append(node.right)
            if l <= node.val <= r:
                sum += node.val
    return sum

# 반복 구조 BFS


def range_sum_bst4(root, l, r):
    queue, sum = [root], 0
    while queue:
        node = queue.pop(0)
        if node:
            if node.val > l:
                queue.append(node.left)
            if node.val < r:
                queue.append(node.right)
            if l <= node.val <= r:
                sum += node.val
    return sum
