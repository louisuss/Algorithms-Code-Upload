# 2 3 5 7
# 4 9 25 49 제곱
# 제곱 * 소수: 8 12 20 28 / 18 27 45 63 /
# 6 10 14 / 15 23 / 35
# 30 42 / 105

# Heap 사용
import heapq
import copy

K, N = map(int, input().split())
a = list(map(int, input().split()))
# lst: heap / ck: 중복수제거
lst, ck = copy.deepcopy(a), set()

heapq.heapify(lst)
# n번째 수
nth = 0


while nth < N:
    minimum = heapq.heappop(lst)
    # 중복되는 경우 2*2*3 == 2*3*2
    if minimum in ck:
        continue
    nth += 1
    ck.add(minimum)
    # heap에 어떤 식으로 수를 넣는게 가장 핵심
    # 2 3 5 7
    # 2 < 2*2
    # 2 < 2*3
    # 2 < 2*5
    # 2 < 2*7
    # 내가 가진수에 어떤 특정 소수를 곱하면 반드시 커진다
    # 2를 체크하기 전에는 뒤에 이어지는 곱을 고려할 필요가 없다

    # lst: 3 5 7 2*2 2*3 2*5 2*7
    # lst: 5 7 2*2 2*3 2*5 2*7 3*2 3*3 3*5 3*7
    for i in a:
        if minimum * i < 2**32:
            heapq.heappush(lst, minimum*i)

print(minimum)
