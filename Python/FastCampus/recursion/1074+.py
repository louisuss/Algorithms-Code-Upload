def z_func(n, r, c):
    global number
    # 2가 최소값임
    if n == 2:
        if r == R and c == C:
            print(number)
            return
        number += 1
        if r == R and c+1 == C:
            print(number)
            return
        number += 1
        if r+1 == R and c == C:
            print(number)
            return
        number += 1
        if r+1 == R and c+1 == C:
            print(number)
            return
        number += 1
        return
    z_func(n/2, r, c)
    z_func(n/2, r, c + n/2)
    z_func(n/2, r + n/2, c)
    z_func(n/2, r + n/2, c + n/2)


number = 0
n, R, C = map(int, input().split())
z_func(2**n, 0, 0)
