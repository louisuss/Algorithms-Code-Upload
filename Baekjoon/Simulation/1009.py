T = int(input())
cases = {
    1: 1,
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: 5,
    6: 6,
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
    0: 10
}

for _ in range(T):
    a, b = map(int, input().split())
    # 끝자리가 중요하므로 1,11,21이 같음
    a = a % 10

    if a == 2 or a == 3 or a == 7:
        print(cases[a][(b % 4)-1])
    elif a == 4 or a == 8 or a == 9:
        print(cases[a][(b % 2)-1])
    else:
        print(cases[a])
