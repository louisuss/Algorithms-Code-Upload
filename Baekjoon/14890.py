from collections import deque

N, L = map(int, input().split())
horizontal_street = [list(map(int, input().split())) for _ in range(N)]
vertical_street = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        vertical_street[i].append(horizontal_street[j][i])

def pass_ok(street):
    start = street[0]
    idx = 1
    temp = 1
    while idx < len(street):
        if start == street[idx]:
            temp += 1
            idx += 1
        elif start == street[idx] - 1:
            if temp < L:
                return False
            else:
                start = street[idx]
                idx += 1
                temp = 1
        elif start == street[idx] + 1:
            i = 0
            # 경사로 하나 놓을 수 있는지 검사
            for _ in range(L):
                # 인덱스 초과하는 경우
                if idx + i >= len(street)
                    return False
                else:
                    # 연속된 값이 아닌경우
                    if street[idx+i] != street[idx]:
                        return False
                    i += 1

            # 현재 경사로 하나를 놓을 수 있는 상황
            # 다음값이 없는 경우 종료
            if idx + L >= len(street):
                return True
            # 다음값이 있는 경우
            # 경사로 개수를 초기화
            # idx 는 현재 바뀐 숫자 위치에 있음
            # start = idx-1 위치에 있음
            else:
                temp = 0
                idx += L
                start = street[idx-1]
        else:
            return False
    return True


sum = 0
for street in horizontal_street:
    sum += pass_ok(street)

for street in vertical_street:
    sum += pass_ok(street)

print(sum)