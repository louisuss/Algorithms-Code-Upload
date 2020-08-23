# 1. 최대 무게까지 dp 만듬
# 2. 각 경우의 수에 대해 합 또는 빼기

n = int(input())
chu = list(map(int, input().split()))
t = int(input())
target = list(map(int, input().split()))

# 최대경우까지
visited = [True] + [False] * (sum(chu))

for c in chu:
    # visited 쓰는 경우
    # IndexError: list index out of range
    # i = 무게 / e = 체크 여부
    for i, e in enumerate(visited[:]):
        # 해당 무게가 체크 된 경우
        if e:
            # 해당 무게 + 추가 추 부분 체크
            if not (visited[i+c]):
                visited[i+c] = True

# [True, True, False, False, True, True]
# print(visited)

# 배는 부분에서 합한 부분에 사용된 추가 빼는 부분에도 사용되지 않는지 의문...
# 합한 부분에 사용된추에 사용된 추는 뺼 때 사용하면 결국엔 안쓴것이됨
# 때문에 영향 없음
for c in chu:
    for i, e in enumerate(visited[:]):
        print(i, e)
        if e:
            # 양수인 부분 중에
            if i-c >= 0:
                # 해당 무게 - 추가 추 부분 체크
                if not(visited[i-c]):
                    visited[i-c] = True

for c in target:
    # 측정하고자하는 추무게가 주어진 총 무게보다 큰경우
    if c > len(visited) - 1:
        print('N', end=' ')
    else:
        if visited[c]:
            print('Y', end=' ')
        else:
            print('N', end=' ')
