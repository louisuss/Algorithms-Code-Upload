def merge_trees(t1, t2):
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = merge_trees(t1.left, t2.left)
        node.right = merge_trees(t1.right, t2.right)

        return node
    else:
        return t1 or t2
