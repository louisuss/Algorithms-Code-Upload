# 1. 각 지그재그 라인별 첫번째 숫자 파악
# 2. 현위치에서 요구대로 이동
# 3. 이동한 위치에 해당하는 지그재그 라인을 N 보다 작은 부분과 큰부분으로 나눔
# 4. 라인 번호를 홀짝으로 나눠 진행 방향을 정함
# 5. 이동한 위치의 값을 시작 숫자와 현재 위치를 기준으로 구함
# 6. 결과값에 합산
# 7. 최종 결과 값 출력

N, K = map(int, input().split())
# 현재 위치
R, C = 1, 1
# 첫번째 등장하는 숫자 1번부터 시작
firstNumbers = [0] * (N * 2)
firstNumbers[1] = 1

def getLength(lineNo):
    # 1 2 3 4 5 6 
    if lineNo <= N:
        return lineNo

    # 5 4 3 2 1
    return N - lineNo % N

for i in range(2, N * 2):
    firstNumbers[i] = firstNumbers[i - 1] + getLength(i - 1)

# [0, 1, 2, 4, 7, 11, 16, 22, 27, 31, 34, 36]
# print(firstNumbers)

def getNumber(r, c):
    lineNumber = r + c - 1
    firstNumber = firstNumbers[lineNumber]
    # 증가
    if lineNumber <= N:
        # 짝수번째 줄
        if lineNumber % 2 == 0:
            # 해당줄에서 값이 증가할수록 r도 증가
            return firstNumber + (r - 1)
        # 홀수번째 줄
        else:
            # 해당줄에서 값이 증가할수록 c도 증가
            return firstNumber + (c - 1)
    # 감소
    else:
        if lineNumber % 2 == 0:
            # 값이 증가할수록 c는 감소
            return firstNumber + (N - c)
        else:
            # 값이 증가할수록 r은 감소
            return firstNumber + (N - r)

result = 1
# 상하좌우 움직이기
for ch in list(input()):
    if ch == 'U':
        R -= 1
    elif ch == 'D':
        R += 1
    elif ch == 'L':
        C -= 1
    elif ch == 'R':
        C += 1
    result += getNumber(R, C)

print(result)

# # 1. 배열판 만들기
# # 2. 움직인 칸 합
# # 3. 합 출력

# n, k = map(int, input().split())
# jumps = list(input())
# fields = [[0]*n for _ in range(n)]
# # U D L R
# dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
# answer = [1]


# def make_zigzag_list(fields, n):
#     cnt = 1
#     fields[0][0] = cnt
#     change_dir = 0

#     for i in range(1, n):
#         if change_dir == 0:
#             for y, x in zip(list(range(i+1)), list(range(i, -1, -1))):
#                 cnt += 1
#                 fields[y][x] = cnt
#             change_dir += 1
#         else:
#             for y, x in zip(list(range(i, -1, -1)), list(range(i+1))):
#                 cnt += 1
#                 fields[y][x] = cnt
#             change_dir -= 1

#     for i in range(1, n):
#         if change_dir == 1:
#             for y, x in zip(list(range(n-1, i-1, -1)), list(range(i, n))):
#                 cnt += 1
#                 fields[y][x] = cnt
#             change_dir -= 1
#         else:
#             for y, x in zip(list(range(i, n)), list(range(n-1, i-1, -1))):
#                 cnt += 1
#                 fields[y][x] = cnt
#             change_dir += 1


# def move(fields, now, dir):
#     y, x = now
#     dy, dx = dirs[dir]
#     ny, nx = y + dy, x + dx
#     answer.append(fields[ny][nx])

#     return (ny, nx)


# make_zigzag_list(fields, n)

# # 움직이기
# now = (0, 0)
# for jump in jumps:
#     now = move(fields, now, jump)
# print(sum(answer))
