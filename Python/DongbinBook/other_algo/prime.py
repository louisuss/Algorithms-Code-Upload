import math

# O(x)


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def is_prime2(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


# 소수 판단이 아니라 수의 범위 안에 모든 소수 찾기
# n 보다 작거나 같은 모든 소수 찾을 때 이용
n = 1000
arr = [True] * (n+1)
for i in range(2, int(math.sqrt(n))+1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

for i in range(2, n+1):
    if arr[i]:
        print(i, end=' ')
