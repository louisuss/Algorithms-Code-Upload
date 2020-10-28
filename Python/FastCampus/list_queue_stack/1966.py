# https://www.acmicpc.net/problem/1966
from collections import deque

n = int(input())

def solution(n):
    for _ in range(n):
        m, wonder = map(int, input().split())
        priority = list(map(int, input().split()))
        result = []
        q = deque([])
        for idx, pt in enumerate(priority):
            q.append((pt, idx))
        
        while q:
            max_value = max(q, key=lambda x: x[0])
            while True:
                if max_value[0] != q[0][0]:
                    q.append(q.popleft())
                else:
                    result.append(q.popleft())
                    break
        for i in range(m):
            if result[i][1] == wonder:
                print(i+1)
                break


def solution2(n):
    m, wonder = map(int, input().split())
    q = list(map(int, input().split()))
    q = [(i, idx) for idx, i in enumerate(q)]
    cnt = 0

    while True:
        if q[0][0] == max(q, key=lambda x: x[0])[0]:
            cnt += 1
            if q[0][1] == m:
                print(cnt)
                break
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))
