n = int(input())

ugly = [0]*n
ugly[0] = 1

# 2, 3, 5배 위한 인덱스
idx2, idx3, idx5 = 0, 0, 0
# 곱셈값 초기화
next2, next3, next5 = 2, 3, 5

# 1 ~ n 까지 못생긴 수 찾기
for num in range(1, n):
    # 가능한 곱셈 결과 중 가장 작은수 선택
    ugly[num] = min(next2, next3, next5)

    # 인덱스 따라 곱셈 결과 증가
    if ugly[num] == next2:
        idx2 += 1
        next2 = ugly[idx2] * 2
    if ugly[num] == next3:
        idx3 += 1
        next3 = ugly[idx3] * 3
    if ugly[num] == next5:
        idx5 += 1
        next5 = ugly[idx5] * 5

    print(num)
    print(ugly)
    print(idx2, idx3, idx5)
    print(next2, next3, next5)
    print()

print(ugly[n-1])
