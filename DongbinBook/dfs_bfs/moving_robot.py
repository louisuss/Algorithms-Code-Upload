from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# Solution1 - 최단거리 -> BFS
def get_next_pos(pos, board):
    next_pos = [] # 반환할 값 (이동 가능한 위치)
    pos = list(pos) # 집합 -> 리스트
    r1, c1 = pos[0]
    r2, c2 = pos[1]

    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    for dr, dc in dirs:
        # 이동 가능한 경우
        nr1, nc1, nr2, nc2 = r1+dr, c1+dc, r2+dr, c2+dc
        if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
            next_pos.append({(nr1, nc1), (nr2, nc2)})
    
    # 가로로 놓인 경우
    if r1 == r2:
        for i in [-1,1]: # 위, 아래 회전
            if board[r1+i][c1] == 0 and board[r2+i][c2] == 0:
                # 회전
                next_pos.append({(r1,c1), (r1+i, r1)})
                next_pos.append({(r2,c2), (r2+i, c2)})
    # 세로로 놓인 경우
    elif c1 == c2:
        for i in [-1,1]:
            if board[r1][c1+i] == 0 and board[r2][c2+i] == 0:
                # 회전
                next_pos.append({(r1,c1), (r1, c1+i)})
                next_pos.append({(r2,c2), (r2, c2+i)})
    
    # 이동할 수 있는 모든 위치 반환
    return next_pos

def solution(board):
    n = len(board)

    # board 범위 넘는 경우 제약
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    
    q = deque()
    visited = []
    start = {(1,1), (1,2)} # 중복 제거하기 위해 집합 사용
    q.append((start, 0))
    visited.append(start)

    while q:
        pos, cost = q.popleft()
        # 목적지 도착 시 종료
        if (n, n) in pos:
            return cost

        # 현재위치에서 이동가능한 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 이동한 위치가 방문하지 않은 위치인 경우
            if next_pos not in visited:
                # 큐 삽입 및 방문 처리
                q.append((next_pos, cost+1))
                visited.append(next_pos)
    return -1

print(solution(board))

    
#Solution2
# dfs 접근법은 최단거리 찾을 때 X

# def rotate(robot, dir):
#     r1, c1 = robot[0]
#     r2, c2 = robot[1]

#     # rotate_up
#     if dir == 0:
#         if board[r1-1][c1] == 0 and board[r2-1][c2] == 0:
#             r1, c1 = r2-1, c2
#             return [(r1, c1), (r2, c2)]
#         else:
#             return []

#     # rotate_down
#     if dir == 1:
#         if board[r1+1][c1] == 0 and board[r2+1][c2] == 0:
#             r1, c1 = r2+1, c2
#             return [(r1, c1), (r2, c2)]
#         else:
#             return []

#     # rotate_right
#     if dir == 2:
#         if board[r1][c1+1] == 0 and board[r2][c2+1] == 0:
#             r2, c2 = r1, c1+1
#             return [(r1, c1), (r2, c2)]
#         else:
#             return []

#     # rotate_left
#     if dir == 3:
#         if board[r1][c1-1] == 0 and board[r2][c2-1] == 0:
#             r2, c2 = r1, c1-1
#             return [(r1, c1), (r2, c2)]
#         else:
#             return []


# dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# def move(robot, visited, cnt, n):
#     # 로봇 현재 위치
#     r1, c1 = robot[0]
#     r2, c2 = robot[1]
#     # 방문 체크 되돌아오는 경우 없애기 위해
#     visited[r1][c1], visited[r2][c2] = True, True

#     # 종료지점 도착시 결과 저장
#     if (r1 == n-1 and c1 == n-1) or (r2 == n-1 and c2 == n-1):
#         result.append(cnt)

#     # 상하좌우 움직이기
#     # 움직이는게 가능한 경우
#     check = 0
#     for dr, dc in dirs:
#         # 움직인 후 로봇 위치
#         nr1, nc1, nr2, nc2 = r1+dr, c1+dc, r2+dr, c2+dc
#         # 필드안에 있는 경우
#         if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n:
#             # 움직인 공간이 벽이 아닌 경우
#             if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
#                 # 둘중한곳을 방문하지 않은 경우 이동 진행
#                 if not visited[nr1][nc1] or not visited[nr2][nc2]:
#                     cnt += 1
#                     move([(nr1, nc1), (nr2, nc2)], visited, cnt, n)
#                     check += 1
#     if check == 0:
#         # 움직이지 못할때 회전
#         for i in range(4):
#             # 모든 방향으로 회전
#             rotated_pos = rotate(robot, i)
#             print(rotated_pos)
#             if rotated_pos:
#                 nr1, nc1 = rotated_pos[0]
#                 nr2, nc2 = rotated_pos[1]

#                 if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n:
#                     if not visited[nr1][nc1] or not visited[nr2][nc2]:
#                         cnt += 1
#                         move([(nr1, nc1), (nr2, nc2)], visited, cnt, n)
#             else:
#                 continue


# def solution(board):
#     start = [(0, 0), (0, 1)]
#     cnt = 0
#     visited = [[False] * n for _ in range(n)]
#     move(start, visited, cnt, n)


# solution(board)
