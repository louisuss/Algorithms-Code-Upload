# N a
# M z
# 사전 알파벳 순서
# 문자열 하나만 찾을수있다

# 2 2 2
# aazz
# azaz
N, M, K = map(int, input().split())
dp = [[1]*101 for _ in range(101)]
dp[1][1] = 2
MAX = 1000000000
ans = ''

for i in range(100):
    for j in range(100):
        if i == 0 or j == 0:
            continue
        a = dp[i][j] * (i+j+1)//(i+1)
        b = dp[i][j] * (i+j+1)//(j+1)

        if a <= MAX:
            dp[i+1][j] = a
        else:
            dp[i+1][j] = MAX+1
        
        if b <= MAX:
            dp[i][j+1] = b
        else:
            dp[i][j+1] = MAX+1


def find_func(N, M, K):
    global ans

    if N == 0:
        ans += 'z'*M
        return
    if M == 0:
        ans += 'a'*N
        return
    if dp[N-1][M] >= K:
        ans += 'a'
        find_func(N-1, M, K)
    else:
        ans += 'z'
        find_func(N, M-1, K-dp[N-1][M])
    return

if dp[N][M] < K:
    print(-1)
else:
    find_func(N, M, K)
    print(ans)


