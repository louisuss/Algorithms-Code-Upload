# 각 행을 차례대로 확인, 각 열에 퀸을 놓는 경우를 고려

# x번째 행에 놓은 queen에 대해서 검증
def check(x):
    # 이전 행에서 놓았던 모든 queen 들을 확인
    for i in range(x):
        # 위쪽 확인. i번째 행 == x번째 행
        if row[x] == row[i]:
            return False
        # 대각선 확인. x번째 행 - i번째 행 == 행 거리
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

# x 번째 행에 대해 처리


def dfs(x):
    global result
    # n번째 행까지 놓을 수 있는 경우
    if x == n:
        result += 1
    else:
        # x 번째 행의 각 열에 queen을 둔다고 가정
        for i in range(n):
            row[x] = i
            print(row)
            # 퀸 놔도 되는 경우
            if check(x):
                # 다음 행 실행
                dfs(x+1)


n = int(input())
row = [0]*n
result = 0
dfs(0)
print(result)


##############
def nqueen(sol, n):
    global cnt

    if len(sol) == n:
        cnt += 1
        return
    
    candidates = list(range(n))
    for i in range(len(sol)):
        if sol[i] in candidates:
            candidates.remove(sol[i])
        distance = len(sol) - i # 행 간의 거리
        if sol[i] + distance in candidates:
            candidates.remove(sol[i]+distance)
        if sol[i] - distance in candidates:
            candidates.remove(sol[i]-distance)
    
    if candidates != []:
        for i in candidates:
            sol.append(i)
            nqueen(sol, n)
    else:
        return

cnt = 0
num = int(input())
for i in range(num):
    nqueen([i], num)
print(cnt)

# dc = [-1, 0, 1]
# def check_possible_case(row, col):
#     if (row >= n or col <= n):
#         return

#     field[row][col] = True
#     print(field)
#     for d in dc:
#         nc = d + col
#         if (0 <= col <n):
#             check_possible_case(row+1, col)

# result = 0
# field = [[False]*n for _ in range(n)]

# for col in range(n):
#     row = 0
#     check_possible_case(row, col) # 체크
#     print(field)
#     # 가능한 경우의수 반복
#     # field 분리 못하면 중복되기 때문에 제대로 처리안됨
#     while row < n-1:
#         row += 1
#         for j in range(n):
#             if not field[row][j]:
#                 check_possible_case(row, j)
