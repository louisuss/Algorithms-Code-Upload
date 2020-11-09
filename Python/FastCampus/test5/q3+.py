from collections import defaultdict, deque

n, k = map(int, input().split())
fountains = list(map(int, input().split()))

# 시간 초과


def solution1():
    setup_positions = defaultdict(bool)
    for fountain in fountains:
        setup_positions[fountain] = True

    setup_cnt = 0
    result = 0
    distance = 1
    while setup_cnt < k:
        check = False
        for fountain in fountains:
            if not setup_positions[fountain-distance]:
                setup_positions[fountain-distance] = True
                result += distance
                setup_cnt += 1
            if setup_cnt == k:
                check = True
                break

            if not setup_positions[fountain+distance]:
                setup_positions[fountain+distance] = True
                result += distance
                setup_cnt += 1
            if setup_cnt == k:
                check = True
                break

        if check:
            break

        distance += 1

    print(result)


solution1()

# BFS 활용


def solution2():
    visited = set(fountains)

    # 모든 샘터의 왼쪽 오른쪽에 대해 확인
    q = deque()
    distance = 1
    for fountain in fountains:
        # (거리, 위치)
        q.append((distance, fountain-distance))
        q.append((distance, fountain+distance))

    setup = 0
    result = 0

    while setup < k:
        dist, now = q.popleft()
        if now in visited:
            continue
        visited.add(now)
        result += dist
        q.append((dist+1, now-1))
        q.append((dist+1, now+1))
        setup += 1

    print(result)


solution2()
