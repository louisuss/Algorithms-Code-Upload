import heapq

n, m = map(int, input().split())
positions = list(map(int, input().split()))
positions.sort()

# 런타임 에러


def solution1():
    minus = []
    plus = []
    for position in positions:
        if position < 0:
            minus.append(position)
        else:
            plus.append(position)

    result = []
    for i in range(0, len(minus), m):
        result.append(-minus[i])
    for i in range(len(plus)-1, -1, -m):
        result.append(plus[i])

    print((sum(result)*2)-(max(-minus[0], plus[-1])))


def solution2():
    positive = []
    negative = []

    largest = max(max(positions), -min(positions))

    # 최대힙
    for position in positions:
        if position > 0:
            heapq.heappush(positive, -position)
        else:
            heapq.heappush(negative, position)

    # 음수로 계산됨
    result = 0

    while positive:
        result += heapq.heappop(positive)
        for _ in range(m-1):
            if positive:
                heapq.heappop(positive)
    while negative:
        result += heapq.heappop(negative)
        for _ in range(m-1):
            if negative:
                heapq.heappop(negative)

    print(-result*2 - largest)


solution1()
solution2()
