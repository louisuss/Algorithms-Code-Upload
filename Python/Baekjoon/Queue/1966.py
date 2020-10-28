# 1. 맨앞 중요도체크 (숫자클수록 높음)
# 2. 중요도 높은 문서있으면 큐뒤로 다시배치 아니면 인쇄
# from collections import deque

# t = int(input())

# for _ in range(t):
#     # 문서 개수 / 문서 위치(0~n-1)
#     n, m = map(int,input().split())
#     temp = list(map(int, input().split()))
#     printer = deque([])
#     order = []
#     # pos, importance
#     for idx, i in enumerate(temp):
#         printer.append((idx, i))

#     while printer:
#         check = False
#         # 중요도 높은거 찾기
#         for i in range(1, len(printer)):
#             if printer[0][1] < printer[i][1]:
#                 check = True
#                 break
#         # 중요도 더 높은것이 존재
#         if check:
#             printer.append(printer.popleft())
#         else:
#             order.append(printer.popleft())
#     for i, v in enumerate(order):
#         if order[i][0] == m:
#             print(i+1)
#             break

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    cnt = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            cnt += 1
            if queue[0][1] == m:
                print(cnt)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
