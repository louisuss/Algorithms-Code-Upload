def knapsack(cargo):
    capacity = 15
    dp = [[0]*(capacity+1) for _ in range(len(cargo)+1)]

    # 넣을 물건
    for i in range(1, len(cargo)+1):
        # 용량
        for j in range(1, capacity+1):
            if cargo[i-1][1] <= j:
                # 이전 가방 가치 + 개수 한개 적을 때 해당가치, 개수 한개 적을 때 해당 가치
                dp[i][j] = max(cargo[i-1][0] + dp[i-1]
                               [j-cargo[i-1][1]], dp[i-1][j])
            else:
                # 이전값 유지
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


print(knapsack([(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)]))


size = [3, 4, 7, 8, 9]
value = [4, 5, 10, 11, 13]

# 1. 하나를 배낭에 넣었을 때 가치의 증가분 + 다음 항목을 검색하는 함수(물론 공간이 줄어듬도 입력)
# 2. 배낭을 넣지 않고 다음을 검색하는 함수


# def knapsack(capacity, n):
#     if capacity == 0 or n == 0:
#         return 0
#     if size[n-1] > capacity:
#         return knapsack(capacity, n-1)
#     else:
#         return max(value[n-1] + knapsack(capacity-size[n-1], n-1), knapsack(capacity, n-1))


# def knapsack1(capacity, n):
#     array = [[0 for _ in range(capacity+2)] for _ in range(n+2)]
#     for i in range(1, n+1):
#         for s in range(1, capacity+1):
#             if size[i-1] > s:
#                 array[i][s] = max(value[i-1] + array[i-1]
#                                   [s-size[i-1]], array[i-1][s])
#                 print('%2d' % array[i][s], end=' ')
#                 print()
#     return array[n][capacity]


# size = [9, 3, 4, 7, 8]
# value = [13, 4, 5, 10, 11]
# print(knapsack1(10, 5))
