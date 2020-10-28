t = int(input())
lst = []
# [0,0] * k * n
s = [[[0]*2 for _ in range(100)] for _ in range(101)]
s[1][0][0] = 1
s[1][0][1] = 1

for n in range(2, 101):
    for k in range(n):
        # 끝이 0 이면 이전 값이 0인 것 1인 것 둘다 가능
        s[n][k][0] = s[n-1][k][0] + s[n-1][k][1]
        # 끝이 1 이면 이전 값이 0인 것, 마지막이 1이라 1이 커질 것이므로 k가 1 작은것 중에 마지막이 1인 것과 합
        s[n][k][1] = s[n-1][k][0] + s[n-1][k-1][1]

for _ in range(t):
    n, k = map(int, input().split())
    print(sum(s[n][k]))
