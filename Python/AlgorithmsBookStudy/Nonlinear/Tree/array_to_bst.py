class TreeNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def array_to_BST(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    # 분할 정복으로 이진 검색 결과 트리 구성
    node = TreeNode(nums[mid])
    node.left = array_to_BST(nums[:mid])
    node.right = array_to_BST(nums[mid+1:])

    return node
