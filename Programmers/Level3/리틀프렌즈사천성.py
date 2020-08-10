def find_route(m1, n1, m2, n2, c):
    up, down, left, right = check_edges(m1, n1, m2, n2, c)
    case = (m1-m2)*(n1-n2)
    if case == 0:
        return (m1 == m2 and up) or (n1 == n2 and left)
    elif case > 0:
        return (up and right) or (down and left)
    else:
        return (up and left) or (down and right)


def check_edges(m1, n1, m2, n2, c):
    up, down, left, right = [True]*4
    for i in range(min(n1, n2), max(n1, n2)+1):
        if matrix[min(m1, m2)][i] not in ('.', c):
            up = False
            break
    for i in range(min(n1, n2), max(n1, n2)+1):
        if matrix[max(m1, m2)][i] not in ('.', c):
            down = False
            break
    for i in range(min(m1, m2), max(m1, m2)+1):
        if matrix[i][min(n1, n2)] not in ('.', c):
            left = False
            break
    for i in range(min(m1, m2), max(m1, m2)+1):
        if matrix[i][max(n1, n2)] not in ('.', c):
            right = False
            break
    return up, down, left, right


m, n = map(int, input().split())
matrix = []
coordinates = {}
for i in range(m):
    row = list(input())
    matrix.append(row)
    for j in range(n):
        c = row[j]
        if c.isupper():
            coordinates.setdefault(c, []).append((i, j))

result = []
friends = sorted(coordinates)
i = 0
while i < len(friends):
    c = friends[i]
    if c in result or c == '.':
        i += 1
        continue
    (m1, n1), (m2, n2) = coordinates[c]
    if find_route(m1, n1, m2, n2, c):
        result.append(c)
        friends[i] = '.'
        matrix[m1][n1] = '.'
        matrix[m2][n2] = '.'
        i = 0
        continue
    i += 1


if len(result) == len(friends):
    print(''.join(result))
else:
    print('IMPOSSIBLE')

# # 기존 프렌즈 사천성 -> 경로가 세 개 이하 선분
# # 리틀 프렌즈 -> 경로가 2개 이하의 수평/수직 선분
# # . 빈칸 / * 막힌칸
# from collections import defaultdict
# from copy import deepcopy


# def delete_line(a, b, board, key):

#     # 선분1
#     x1, y1 = a
#     x2, y2 = b

#     check = True
#     # 같은 행 위치
#     if x1 == x2:
#         for i in range(y1+1, y2):
#             if board[x1][i] != '.':
#                 check = False
#                 break
#         if check:
#             board[x1][y1], board[x2][y2] = '.', '.'
#             print(board)
#             return key

#     # 같은 열 위치
#     elif y1 == y2:
#         for i in range(x1+1, x2):
#             if board[i][y1] != '.':
#                 check = False
#                 break
#         if check:
#             board[x1][y1], board[x2][y2] = '.', '.'
#             return key
#     # 선분2

#     check1, check2 = True, True
#     # 왼쪽에 있는 경우
#     if x1 < x2 and y1 > y2:
#         # 두 방향이 있음
#         for i in range(y2, y1):
#             if board[x1][i] != '.':
#                 check1 = False
#                 break
#         if check1:
#             for i in range(x1, x2):
#                 if board[i][y2] != '.':
#                     check1 = False
#                     break

#         for i in range(x1+1, x2+1):
#             if board[i][y1] != '.':
#                 check2 = False
#                 break
#         if check2:
#             for i in range(y2+1, y1+1):
#                 if board[x2][i] != '.':
#                     check2 = False
#                     break

#     elif x1 < x2 and y1 < y2:
#         for i in range(y1+1, y2+1):
#             if board[x1][i] != '.':
#                 check1 = False
#                 break
#         if check1:
#             for i in range(x1, x2):
#                 if board[i][y2] != '.':
#                     check1 = False
#                     break

#         for i in range(x1+1, x2+1):
#             if board[i][y1] != '.':
#                 check2 = False
#                 break
#         if check2:
#             for i in range(y1+1, y2):
#                 if board[x2][i] != '.':
#                     check2 = False
#                     break

#     if check1 and check2:
#         board[x1][y1], board[x2][y2] = '.', '.'
#         return key


# def solution(m, n, board):
#     answer = []
#     board = list(map(list, board))
#     positions = defaultdict(list)

#     for i in range(m):
#         for j in range(n):
#             if ord(board[i][j]) in list(range(ord('A'), ord('Z')+1)):
#                 positions[board[i][j]].append((i, j))

#     while True:
#         before_answer = deepcopy(answer)
#         temp = []
#         for a, b in positions.values():
#             t = delete_line(a, b, board, board[a[0]][a[1]])
#             if t != None:
#                 temp.append(t)
#         if temp:
#             answer.extend(sorted(temp))

#         if len(answer) == len(positions):
#             return ''.join(answer)
#         else:
#             if before_answer == answer:
#                 return "IMPOSSIBLE"


# m = 3
# n = 3
# board = ['DBA', 'C*A', 'CDB']
# print(solution(m, n, board))

# a=[[1,2],[3,4]]
# a[0][1] = 3
# print(a)
# # 특정 문자 조건 찾기
# # print(list(range(ord('A'), ord('Z')+1)))

# # 문자열 1개씩 가져오는지?
# # print(board[0][0])
# # for v in 'abc':
# #     print(v)

# # 문자열 부분 리스트로 변환하기
# # board = list(map(list, board))
# # board = [list(b) for b in board]
# # print(board)
