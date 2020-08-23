# 00 01 02
# 10 11 12
# 20 21 22
# 30 31 32

# # 최소값은 간선 한번이 최소임
# 왼쪽값: 10 = sum(01,10)
# 중간값: 11 = sum(01,11)
# 오른쪽값: 12 = sum(01,12)

# 왼쪽값: 20 = min(sum(10,20), sum(11,20))
# 중간값: 21 = min(sum(10,21),sum(11,21),sum(12,21))
# 오른쪽값: 22 = min(sum(11,22),sum(12,22))

test_num = 1
while True:
    node_num = int(input())
    if not node_num or node_num < 2:
        break

    # node_num을 1부터 시작하기 위해
    routes = [[0]*3] + [list(map(int, input().split()))
                        for _ in range(node_num)]
    dp = [[0]*3 for _ in range(node_num+1)]
    dp[1] = routes[1]
    dp[2] = [dp[1][1]+routes[2][0], dp[1][1]+routes[2][1], dp[1][1]+routes[2][2]]

    if node_num == 2:
        print("{}. {}".format(test_num, dp[node_num][1]))
    else:
        for i in range(3, node_num+1):
            dp[i][0] = min([dp[i-1][0], dp[i-1][1]]) + routes[i][0]
            dp[i][1] = min([dp[i-1][0], dp[i-1][1], dp[i-1][2]]) + routes[i][1]
            dp[i][2] = min([dp[i-1][1], dp[i-1][2]]) + routes[i][2]
        print("{}. {}".format(test_num, dp[node_num][1]))

    test_num += 1
