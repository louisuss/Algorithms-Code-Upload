t = int(input())

for _ in range(t):
    n = int(input())
    # 1: open / 0: close
    dp = [0] + [1]*(n)

    # n번째 라운드
    for i in range(2, n+1):
        # 방번호
        for j in range(1, n+1):
            if j % i == 0:
                if dp[j] == 1:
                    dp[j] = 0
                else:
                    dp[j] = 1
    print(dp.count(1))
