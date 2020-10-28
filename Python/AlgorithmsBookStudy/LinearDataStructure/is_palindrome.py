from collections import deque


def isPalindrome(head):
    q = deque([])

    # head가 없는 경우
    if not head:
        return True

    node = head
    # 리스트 반환
    while node:
        # 현재 노드 추가
        q.append(node.val)
        # 다음 노드 저장
        node = node.next

    while len(q) > 1:
        # 좌우 뽑기
        if q.popleft() != q.pop():
            return False
    return True

# 런너 이용


def is_palindrome(head):
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 연결리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev
