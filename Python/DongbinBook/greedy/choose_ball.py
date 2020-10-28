from itertools import combinations

n, m = map(int, input().split())
kg = list(map(int, input().split()))

# Solution1
cnt = 0
for case in combinations(kg, 2):
    if case[0] != case[1]:
        cnt += 1
print(cnt)

# Solution2
arr = [0]*11
# 해당하는 무게 개수 카운트
for x in kg:
    arr[x] += 1

result = 0
# 각 무게에 대해 처리
for i in range(1, m+1):
    # 공 갯수. 무게가 i인 공 개수(A가 선택할 수 있는 개수) 제외
    n -= arr[i]
    result += arr[i] * n  # B가 선택할 수 있는 경우
print(result)
