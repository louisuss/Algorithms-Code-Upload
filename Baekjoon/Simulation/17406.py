from copy import deepcopy

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = [list(map(int, input().split())) for _ in range(k)]
# 남 서 북 동
dx, dy = [1,0,-1,0], [0,-1,0,1]
ans = 10000

def value(arr):
    return min([sum(i) for i in arr])

def convert(arr, qry):
    r,c,s = qry
    # 중앙에서 시작해서 오른쪽 대각선 방향부터 시작
    r, c = r-1, c-1
    new_arr = deepcopy(arr)
    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for w in range(4):
            for d in range(i*2):
                rrr, ccc = rr + dx[w], cc + dy[w]
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc
    return new_arr

# check 배열 대신 비트 마스크를 활용하여 쿼리를 체크했는지 확인 가능
def dfs(arr, qry):
    global ans
    # 쿼리다처리
    print(qry)
    print(sum(qry))
    if sum(qry) == k:
        ans = min(ans, value(arr))
        return
    for i in range(k):
        if qry[i]:
            continue
        new_arr = convert(arr, q[i])
        # 백트래킹 - 쿼리 처리했다하고 다시 쿼리 처리 안한 상태로 바꿈
        qry[i] = 1
        dfs(new_arr, qry)
        qry[i] = 0

dfs(a, [0 for i in range(k)])
print(ans)



