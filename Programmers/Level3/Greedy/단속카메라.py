from copy import deepcopy


def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000
    answer = 0

    for route in routes:
        if last_camera < route[0]:

            answer += 1
            last_camera = route[1]
    return answer

# def solution(routes):
#     answer = 0
#     routes.sort()

#     standard = routes[0][1]
#     routes.pop(0)
#     answer += 1

#     for item in routes:
#         if item[0] <= standard:
#             standard = min(item[1], standard)
#         else:
#             standard = item[1]
#             answer += 1
#     return answer

# return 최소 카메라 설치 갯수

# 차량: 1~ 10000
# [진입, 진출]
# 진입, 진출 지점에 카메라 설치도 만난 것
# -30000 ~ 진입, 진출 ~ 30000


# 교점이 많은 부분에 설치하는게 이득


# def solution(routes):
#     answer = 0
#     n = len(routes)
#     check = [0] * n
#     start = sorted(routes, key=lambda x: x[0])[0][0]
#     end = sorted(routes, key=lambda x: x[1])[-1][1]

#     checked = set()
#     # 전체 구간
#     for idx in range(start, end+1):
#         new_checked = deepcopy(checked)
#         # for i,s,e in enumerate(routes): -> 에러
#         # 특정 구간에서 감시 가능한 차 체크
#         for i, v in enumerate(routes):
#             if v[0] <= idx <= v[1]:
#                 checked.add(i)
#         # 모두 커버 가능한 경우 종료
#         if len(checked) == n:
#             return answer

#         # 집합 관계로 문제 풀이해야 함
#         if checked != new_checked:
#             pass
#         else:
#             answer += 1
