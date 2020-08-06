cnt0 = [1, 0, 1] # 0 개수 - 2 = 0 + 1
cnt1 = [0, 1, 1] # 1 개수 - 2 = 0 + 1

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

# 시간 초과

# t = int(input())

# def fibo(n):
#     if n == 0:
#         return '0'
#     elif n == 1:
#         return '1'
#     else:
#         return fibo(n-1) + fibo(n-2)


# count = []
# for _ in range(t):
#     n = int(input())
#     count.append((fibo(n).count('0'), fibo(n).count('1')))
# for c in count:
#     print('{} {}'.format(c[0], c[1]))
