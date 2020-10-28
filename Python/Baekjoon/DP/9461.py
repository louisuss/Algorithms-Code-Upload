t = int(input())

def tri_cnt(n):
    cnt = [1,1,1]
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        for i in range(3, n+1):
            cnt.append(cnt[i-3] + cnt[i-2])
        return cnt[n]

for _ in range(t):
    n = int(input())
    print(tri_cnt(n-1))