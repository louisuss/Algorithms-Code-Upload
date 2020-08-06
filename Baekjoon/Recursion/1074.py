def solve(n, r, c):
    global result
    if n == 2:
        if r == R and c == C:
            print(result)
            return
        result+=1
        if r == R and c + 1 == C:
            print(result)
            return
        result+=1
        if r + 1 == R and c == C:
            print(result)
            return
        result+=1
        if r + 1 == R and c+1 == C:
            print(result)
            return
        result += 1
        return
    solve(n/2, r, c)
    solve(n/2, r, c+n/2)
    solve(n/2, r+n/2, c)
    solve(n/2, r+n/2, c+n/2)

result = 0
N, R, C = map(int, input().split(' '))
solve(2**N, 0, 0)