
# 3 X 3 이 아닌 다양한 유형으로 출제 가능
# 첫번째 점이 뒤집히는지알면 두번째 점이 뒤집혀야되는지 파악 가능

N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]


def flip(x, y, A):
    for i in range(3):
        for j in range(3):
            # XOR ^=
            A[x+i][y+j] ^= 1


ans = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(i, j, A)
            ans += 1
if A != B:
    print(-1)
else:
    print(ans)
