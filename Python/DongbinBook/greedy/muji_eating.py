import heapq

food_times = list(map(int, input().split()))
k = int(input())


def solution(food_times, k):
    # 전체 음식 먹는 시간보다 k가 크거나 같으면 -1
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        # 음식시간, 번호
        heapq.heappush(q, (food_times[i], i+1))
    sum_value = 0
    prev = 0
    length = len(food_times)

    # 현재음식시간-이전음식시간 * 현재 음식 개수
    while sum_value + ((q[0][0]-prev)*length) <= k:
        now = heapq.heappop(q)[0]  # 현재 음식 시간
        sum_value += (now - prev) * length
        length -= 1  # 다먹은음식 제외
        prev = now
    result = sorted(q, key=lambda x: x[1])
    print(result)
    return result[(k-sum_value) % length][1]


def solution2(food_times, k):
    n = len(food_times)
    if sum(food_times) <= k:
        return -1

    def move_next(idx):
        if food_times[idx] == 0:
            idx = (idx+1) % n
            # 0이 아닌 곳을 만나는 경우 탈출
            while food_times[idx] == 0:
                idx = (idx+1) % n
            return idx
        else:
            return idx
    time = 0
    idx = 0
    n = len(food_times)
    while time < k:
        food_times[idx] -= 1
        idx = move_next((idx + 1) % n)
        time += 1

    return idx+1


print(solution2(food_times, k))
