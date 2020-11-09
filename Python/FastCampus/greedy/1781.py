import heapq

# 시간초과


def solution1(dead_cups):
    dead_cups = sorted(dead_cups, key=lambda x: (x[0], -x[1]), reverse=True)

    now, result = dead_cups.pop()

    while dead_cups:
        deadline, cup = dead_cups.pop()
        if deadline != now:
            now = deadline
            result += cup
    print(result)


def solution2():
    q = []
    dead_cups.sort()
    for deadline, cup in dead_cups:
        heapq.heappush(q, cup)
        # deadline 초과하는 경우 최소 원소 제거
        if deadline < len(q):
            heapq.heappop(q)

    print(sum(q))


n = int(input())
dead_cups = []
for _ in range(n):
    deadline, cup = map(int, input().split())
    dead_cups.append((deadline, cup))

solution1(dead_cups)
solution2()
