MAX_VALUE = 10000000  # 최대값 제한
a_distance, b_distance, a, b = map(int, input().split())

check = False
while a < MAX_VALUE:
    if a == b:
        check = True
        break
    elif a < b:
        a += a_distance
    else:
        b += b_distance

if check:
    print(a)
else:
    print(-1)
