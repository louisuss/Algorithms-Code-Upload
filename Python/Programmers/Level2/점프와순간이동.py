def solution(n):
    return bin(n).count('1')

# k칸 점프 (건전지 소모)
# 현재 온거리*2
# 백트래킹 ?
# 2500 1250 625


def solution(n):
    ans = 1

    while n != 1:
        ans += n % 2
        n //= 2

    return ans


def solution(n):
    return bin(n).count('1')
