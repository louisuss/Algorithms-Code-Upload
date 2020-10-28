# 재귀
def reverse_list(head):
    def reverse(node, prev):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    return reverse(head)

# 반복


def reverse_list2(head):
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev
