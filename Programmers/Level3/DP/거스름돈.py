# dp[y][x] = y: 거스름돈 가능 화폐 / x: 0~n원까지의 금액


def solution(n, money):
    dp = [[0]*(n+1) for _ in range(len(money))]
    dp[0][0] = 1

    # 동전의 최솟값으로 만들 수 있는 값들, 최소 동전이 1이 아닌 경우도 있을 수 있음
    for i in range(money[0], n+1, money[0]):
        dp[0][i] = 1

    for y in range(1, len(money)):
        # n원 까지 반복
        for x in range(n+1):
            # x원이 money[y] 보다 클 때 새로운 경우의 수 가능
            if x >= money[y]:
                # 이전화폐로 가능한 경우 + 구하는 금액-현재화폐에 해당하는 금액
                dp[y][x] = (dp[y-1][x] + dp[y]
                            [x-money[y]]) % 1000000007
            # 값이 더 커서 갱신 안됨
            else:
                dp[y][x] = dp[y-1][x]

    return dp[-1][-1]
