from collections import deque


def move(cur1, cur2, board):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ret = []

    for y, x in dirs:
        if board[cur1[0]+y][cur1[1]+x] == 0 and board[cur2[0]+y][cur2[1]+x] == 0:
            ret.append({(cur1[0]+y, cur1[1]+x), (cur2[0]+y, cur2[1]+x)})

    rotate = [1, -1]
    # 가로로 위치해있는 로봇 회전
    if cur1[0] == cur2[0]:
        for r in rotate:
            if board[cur1[0]+r][cur1[1]] == 0 and board[cur2[0]+r][cur2[1]] == 0:
                ret.append({(cur1[0]+r, cur1[1]), (cur1[0], cur1[1])})
                ret.append({(cur2[0]+r, cur2[1]), (cur2[0], cur2[1])})
    # 세로로 위치해있는 로봇 회전
    else:
        for r in rotate:
            if board[cur1[0]][cur1[1]+r] == 0 and board[cur2[0]][cur2[1]+r] == 0:
                ret.append({(cur1[0], cur1[1]), (cur1[0], cur1[1]+r)})
                ret.append({(cur2[0], cur2[1]), (cur2[0], cur2[1]+r)})

    return ret


def solution(board):
    size = len(board)

    # 상하좌우 경계값 추가하기 때문에 +2
    new_board = [[1]*(size+2) for _ in range(size+2)]
    for i in range(size):
        for j in range(size):
            new_board[i+1][j+1] = board[i][j]

    queue = deque()
    visited = []

    # [로봇 좌표정보, 지금까지 거리]
    # set 형식으로 해줘야 시간 통과
    queue.append([{(1, 1), (1, 2)}, 0])
    visited.append({(1, 1), (1, 2)})

    while queue:
        q = queue.popleft()
        cur = list(q[0])
        dist = q[1] + 1

        for m in move(cur[0], cur[1], new_board):
            if (size, size) in m:
                return dist
            if not m in visited:
                queue.append([m, dist])
                visited.append(m)
    return 0
