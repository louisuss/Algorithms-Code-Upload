from collections import deque
from itertools import permutations

# 친구 투입 후 다음 친구 투입


def nxt_idx(queue, d, start_idx=0):
    # 시작점
    start_num = queue[start_idx]
    # i = 거리
    for i in range(1, d+1):
        try:
            # 이동 가능 거리 안에서 다음 취약점 포함되는 경우
            if queue[start_idx + 1] == start_num + i:
                start_idx = start_idx + 1
        # 예외처리 안하는 경우 런타임 에러뜸
        except:
            break

    # 시작점을 이동하고 난 후 체크된 취약점 이외부터 시작
    return start_idx+1


def solution(n, weak, dist):
    dist.sort(reverse=True)
    weak = deque(weak)

    # 투입 친구 수
    for i in range(1, len(dist)+1):
        if i == 1:
            # 모든 취약점 지점에서 진행
            for _ in range(len(weak)):
                # 가장 많이 움직이는 친구 1명
                d = dist[0]
                # 총 이동 가능거리가 넉넉한 경우
                if weak[-1] <= weak[0] + d:
                    return 1
                else:
                    # 약한 지점만큼 회전하므로 원래 상태로 돌아감
                    weak.rotate(-1)
                    # 왼쪽 방향 회전 - 마지막 수 = 마지막 수 + 원 길이
                    weak[-1] = weak[-1] + n

            weak = deque(map(lambda x: x % n, weak))
        # 친구 1명 보다 2명이상 투입하는 경우
        else:
            # 투입되는 친구 리스트 조합
            dist2 = list(permutations(dist[:i]))
            for selected in dist2:
                for _ in range(len(weak)):
                    # 시작점 인덱스
                    start_idx = 0
                    # 친구 선택
                    for d in selected:
                        # weak list, 친구 커버 가능 길이, 시작점 인자로 전달해서 새로운 시작점 구함
                        start_idx = nxt_idx(weak, d, start_idx)
                        # 시작점이 다 경로에 도달한 경우
                        if start_idx == len(weak):
                            return i
                    # 모든 경우에 대해 조건 만족하지 않는 경우 weak 회전
                    weak.rotate(-1)
                    weak[-1] = weak[-1] + n
                # 처음 상태 weak로 복구
                weak = deque(map(lambda x: x % n, weak))
    return -1


MAX = 8


# (처리가능 영역, 취약점 리스트)
def shift(N, arr):
    # item = 취약점 리스트
    # [1,5,6,10]
    # 1 item - arr[0] = 0
    # 5 5-1 = 4
    # 6 6-1 = 5
    # 10 10-1 = 9
    # 각 취약점 별로 초기값 부터의 거리 리스트 / 취약점이 초기값 보다 작은 경우 처리가능 영역만큼 더함
    return [item - arr[0] if item >= arr[0] else item - arr[0] + N for item in arr]


# 다음 친구 투입
def recursive(weak, dist, num):
    # 이미 이전 친구가 다 커버한 경우
    if len(weak) == 0:
        return num
    # 더 이상 일할 친구가 없는 경우
    if len(dist) == 0:
        return MAX

    val = MAX
    # 다음으로 일 할 친구 바꿔가면서 반복해서 해당 인원으로 커버 가능한지 체크
    for i in range(len(dist)):
        j = 0
        while j < len(weak) and dist[i] + weak[0] >= weak[j]:
            j += 1
        # 친구 1명 투입해서 끝내지 못한 경우 다음 친구가 이어서 처리 -> 일 마무리 되면 val 값에 친구 수가 입력되서 리턴
        # i번째 친구 제외 후 다음 친구로 반복
        val = min(val, recursive(weak[j:], dist[:i] + dist[i+1:], num + 1))
    return val


def solution(n, weak, dist):
    answer = MAX
    # 최대 처리가능 영역
    max_dist = dist.pop()

    # 취약점 개수만큼 반복
    for i in range(len(weak)):
        # 인자: 총 영역, 취약점 리스트
        tmp = shift(n, weak)
        # 최고 이동 가능한 친구
        d = max_dist
        j = 0
        # 첫번째 친구 투입
        # 인덱스가 취약점 길이보다 작고 시작점부터 커버 가능 거리가 증가되는 인덱스 위치의 취약점 보다 큰경우 -> 커버 가능영역이라 인덱스 +
        while j < len(tmp) and d + tmp[0] >= tmp[j]:
            j += 1

        # 인자로 다음친구가 처리해야될 weak 부분, 이동가능 거리 리스트, 현재 친구 수 넘김
        answer = min(answer, recursive(tmp[j:], dist, 1))
        # weak 회전
        weak = weak[1:] + [weak[0]]

    # MAX 값이 그대로 유지된 경우는 해결 못한 경우임
    if answer == MAX:
        answer = -1

    return answer
