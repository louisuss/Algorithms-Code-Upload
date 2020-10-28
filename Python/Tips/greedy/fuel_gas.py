# %연산으로 원형리스트 회전

# O(n**2)
def complete_circle(gas, cost):
    for start in range(len(gas)):
        fuel = 0
        for i in range(start, len(gas)+start):
            index = i % len(gas)

            can_travel = True
            if gas[index] + fuel < cost[index]:
                break
            else:
                fuel += gas[index] - cost[index]
        if can_travel:
            return start
    return -1


def complete_circle2(gas, cost):
    # 예외조건 제거
    if sum(gas) < sum(cost):
        return False

    # 순차 탐색
    start, fuel = 0, 0
    for i in range(len(gas)):
        # 출발점이 안되는 지점
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    return start
