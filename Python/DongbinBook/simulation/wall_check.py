from itertools import permutations
n = int(input())
weak = list(map(int, input().split()))
dist = list(map(int, input().split()))


def solution(n, weak, dist):
    weak_len = len(weak)
    # 가장 많이 움직일 수 있는 친구 순으로 사용
    dist.sort(reverse=True)
    # 원형 -> 일자형 = 길이 2배 늘림
    for i in range(weak_len):
        weak.append(weak[i]+n)

    # 최소값 구하기위해 최대값 + 1으로 초기화
    answer = len(dist) + 1

    # 0부터 길이만큼의 모든 위치를 시작점으로 설정
    # 취약 위치만을 시작점으로 설정하면 오류??

    for start in range(weak_len):
        # 친구를 나열할 수 있는 모든 경우의 수
        # 모든 친구 조합의 경우의 수에 대해 고려해야하는지 의문. 최고로 많이 돌아다니는 친구 먼저 활용하는게 맞지않나?

        # for friends in permutations(dist, len(dist)):
        friend_cnt = 1  # 투입친구 수
        # 해당 친구가 점검할 수 있는 마지막 위치

        # last_position = weak[start] + friends[friend_cnt-1]
        last_position = weak[start] + dist[friend_cnt-1]

        # 시작점부터 모든 취약점 확인
        # 마지막 위치 인덱스 찾기 위해 반복문 실행
        for idx in range(start, start + weak_len):
            # 모든 취약점 처리 못한 경우 반복
            if last_position < weak[idx]:
                friend_cnt += 1  # 친구 추가 투입
                # 추가 투입 인원이 친구 인원보다 큰 경우 종료
                if friend_cnt > len(dist):
                    break
                # weak[idx]를 시작점으로 친구가 처리할 수 있는 만큼 처리한 위치가 마지막 위치
                last_position = weak[idx] + dist[friend_cnt-1]
        # 종료지점까지 투입된 모든 인원수 비교
        answer = min(answer, friend_cnt)

    if answer > len(dist):
        return -1
    else:
        return answer


print(solution(n, weak, dist))
