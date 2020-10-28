def swap_pairs(head):
    cur = head

    while cur and cur.next:
        # 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        # 인덱스 위치 변경
        cur = cur.next.next

    return head


def swap_pairs2(head):
    root = prev = [None]
    prev.next = head
    # b가 a(head)를 가리키도록 할당
    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        # prev가 b를 가리키도록 할당
        prev.next = b

        # 다음번 비교를 위해 이동
        head = head.next
        prev = prev.next.next
    return root.next


def swap_pairs3(head):
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴
        head.next = swap_pairs3(p.next)
        p.next = head
        return p
    return head
