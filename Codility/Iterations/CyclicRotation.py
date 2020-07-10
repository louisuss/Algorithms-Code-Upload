from collections import deque


def solution(A, K):
    if len(A) == 0:
        return A
    elif len(A) == K or len(set(A)) == 1:
        return A
    else:
        A = deque(A)
        for _ in range(K):
            A.appendleft(A.pop())
        return list(A)
