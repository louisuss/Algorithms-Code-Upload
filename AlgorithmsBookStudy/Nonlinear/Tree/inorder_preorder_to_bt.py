def build_tree(preorder, inorder):
    if inorder:
        # 전위 순회 결과는 중위 순회 분할 인덱스
        index = inorder.index(preorder.pop(0))

        # 중위 순회 결과 분할 정복
        node = TreeNode(inorder[index])
        node.left = build_tree(preorder, inorder[0:index])
        node.right = build_tree(preorder, inorder[index+1:])

        return node
