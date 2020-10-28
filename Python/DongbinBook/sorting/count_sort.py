# 동일한 값 가지는 데이터 여러 개 등장할 때 유용
# O(N+K)
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 0, 3, 1, 6]

cnt = [0] * (max(arr) + 1)

for i in arr:
    cnt[i] += 1

for i in range(len(cnt)):
    # i를 cnt 만큼 출력
    for j in range(cnt[i]):
        print(i, end=' ')
