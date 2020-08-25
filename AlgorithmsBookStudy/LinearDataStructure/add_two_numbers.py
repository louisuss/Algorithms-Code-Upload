class Solution:
    # 연결 리스트 뒤집기
    def reverse_list(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    # 연결리스트 -> 파이썬 리스트
    def to_list(self, node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def to_reversed_linked_list(self, result):
        prev = None
        for r in result:
            node = [r]
            node.next = prev
            prev = node

        return node

    def add_two_numbers(self, l1, l2):
        a = self.to_list(self.reverse_list(l1))
        b = self.to_list(self.reverse_list(l2))

        result_str = int(''.join(str(e) for e in a)) + \
            int(''.join(str(e) for e in b))

        return self.to_reversed_linked_list(str(result_str))
