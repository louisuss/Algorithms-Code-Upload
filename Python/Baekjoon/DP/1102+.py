# 발전소 개수 1 <= N <= 16
# 0 <= P <+ N
# 오류

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
check = list(input())
p = int(input())
dp = [[] for _ in range(n)]
cnt_y = 0


for i, ck in enumerate(check):
    if ck == 'Y':
        for j in range(n):
            if i != j and check[j] == 'N':
                dp[j].append(lst[i][j])

new_dp = []
for d in dp:
    if d:
        new_dp.append(min(d))

if p <= check.count('Y'):
    print(0)
else:
    need_fix = p - check.count('Y')
    if need_fix <= len(new_dp):
        print(sum(sorted(new_dp)[:need_fix]))
    else:
        print(-1)
