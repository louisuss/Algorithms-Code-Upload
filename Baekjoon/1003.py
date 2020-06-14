cnt0 = [1, 0]
cnt1 = [0, 1]

def fibo(n):
    length = len(cnt0)
    if length <= n:
        for i in range(length, n+1):
            cnt0.append(cnt0[i-1]+cnt0[i-2])
            cnt1.append(cnt1[i-1]+cnt1[i-2])
    print("{} {}".format(cnt0[n], cnt1[n]))

t = int(input())
for i in range(t):
    n = int(input())
    fibo(n)
