test_case = int(input())
data_list = list()

for _ in range(test_case):
    # H, W, N
    H, W, N = map(int,input().split())
    a = N % H
    b = N // H + 1
    if a == 0:
        a = H
        b -= 1
    print(a*100+b)

