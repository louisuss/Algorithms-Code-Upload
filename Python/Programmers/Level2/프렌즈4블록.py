# 1. 2*2 지우기
# 2. 내리기
# 3. 2*2 지우기
# 4. 더이상 없으면 정지하고 결과 리턴
# m : 높이 n : 폭

from copy import deepcopy


def down(m, n, board):
    # 행 순회
    for i in range(n):
        temp = []
        # 1이 아닌 부분을 임시 리스트에 넣음
        for j in range(m):
            if board[j][i] != 1:
                temp.append(board[j][i])
        # i 열의 리스트에 역으로 temp 리스트를 pop 나머지는 1로 채움
        for j in range(m-1, -1, -1):
            if len(temp):
                board[j][i] = temp.pop()
            else:
                board[j][i] = 1
    return board


def delete(m, n, board):
    temp = deepcopy(board)
    dir = [(1, 0), (0, 1), (1, 1)]

    for i in range(m-1):
        for j in range(n-1):
            cnt = 1
            for x, y in dir:
                ny, nx = (i + y), (j + x)

                if board[ny][nx] == board[i][j]:
                    cnt += 1

            if cnt == 4:
                temp[i][j] = 1
                for x, y in dir:
                    nx, ny = j + x, i + y
                    temp[ny][nx] = 1

    return down(m, n, temp)


def count(m, n, board):
    total = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                total += 1
    return total


def solution(m, n, board):
    answer = 0
    board = list(map(list, board))

    while True:
        temp = delete(m, n, board)
        if board == temp:
            break
        else:
            board = temp

    return count(m, n, board)
