# 5
# 8
# 1 0 0 1
# 1 1 1 1
# 2 1 0 1
# 2 2 1 1
# 5 0 0 1
# 5 1 0 1
# 4 2 1 1
# 3 2 1 1

# 주어진 프레임으로 설치 및 삭제 후 판단해서 해당 옵션 사용 여부 판단

n = int(input())
frame_cnt = int(input())
build_frame = []
for _ in range(frame_cnt):
    # x: 가로, y: 세로, a: 종류 b: 설치 삭제 유무
    x, y, a, b = map(int, input().split())
    build_frame.append([x, y, a, b])

# 현재 설치된 구조물이 가능한지 여부 체크


def possible(answer):
    for x, y, stuff in answer:
        # 기둥
        if stuff == 0:
            # 바닥위, 보의 한쪽 끝 부분(2가지), 다른 기둥 위
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        # 보
        else:
            # 한쪽 끝부분이 기둥(2가지), 양쪽 끝부분이 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        # 삭제
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        # 설치
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)


print(solution(n, build_frame))


# 오류
# 해당 프레임이 순차적으로 입력되어 전체적인 경우에 대해 조치를 못취함

# def solution(n, build_frame):
#     field = [[0]*n for _ in range(n)]
#     result = []

#     # 기둥 설치 함수
#     def make_top(x, y):
#         # 바닥위, 보 한쪽끝, 다른 기둥 위
#         if y == 0 or field[y][x] == 2 or field[y][x] == 1:
#             field[y][x], field[y+1][x] = 1, 1
#             return True
#         return False

#     # 보 설치 함수
#     def make_right(x, y):
#         # 한쪽끝 기둥, 양쪽 끝부분이 다른보와 연결
#         if field[y][x] == 1 or field[y][x+1] == 1 or field[y][x] == 2 and field[y][x+1] == 2:
#             field[y][x], field[y][x+1] = 2, 2
#             return True
#         return False

#     # 기둥 삭제 함수
#     def del_top(x,y):
#         if field[y+1][x] != 0:
#             return False
#         else:
#             field[y+1][x] = 0
#             return True

#     # 보 삭제 함수
#     def del_right(x, y):
#         if field[y][x] != 0 and field[y][x+1] != 0:
#             return False
#         else:
#             field[y][x+1] = 0
#             return True

#     for frame in build_frame:
#         x, y, a, b = frame

#         # 설치하는 경우
#         if b == 1:
#             # 기둥 설치
#             if a == 0:
#                 if make_top(x, y):
#                     result.append([x, y, a])
#             # 보 설치
#             else:
#                 if make_right(x, y):
#                     result.append([x, y, a])
#         else:
#             # 기둥 삭제
#             if a == 0:
#                 del_top(x, y)
#             # 보 삭제
#             else:
#                 del_right(x, y)

#     result.sort(key=lambda x: (x[0], x[1], x[2]))
#     print(result)
