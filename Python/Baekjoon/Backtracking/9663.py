# x번째 행에 놓은 Queen 검증
def check(x):
    # 이전행에서 놓았던 모든 Queen들 확인
    for i in range(x):
        # 위쪽 혹은 대각선 확인
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
    return True

# x번째 행에 대해 처리
def dfs(x):
    print(x)
    global result
    print(result)
    if x == n:
        result += 1
    else:
        # x번째 행의 각 열에 Queen을 둔다고 가정
        for i in range(n):
            row[x] = i
            print(row)
            # 해당 위치에 Queen 놔도 되는 경우
            if check(x):
                dfs(x+1)

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)
