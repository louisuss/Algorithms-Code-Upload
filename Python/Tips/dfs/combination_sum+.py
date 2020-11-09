result = []
candidates = list(map(int, input().split()))
target = int(input())


def dfs(csum, idx, path):
    # 종료조건
    if csum < 0:
        return
    if csum == 0:
        result.append(path)
        return

    for i in range(idx, len(candidates)):
        # 다음으로 자기 자신을 포함하고 마지막길이까지의 숫자를 선택 가능
        dfs(csum-candidates[i], i, path + [candidates[i]])


dfs(target, 0, [])
print(result)


def comb_sum(candidates, target):
    result = []

    def dfs(csum, idx, path):
        if csum > target:
            return
        if csum == target:
            result.append(path)
            return
        for i in range(idx, len(candidates)):
            dfs(csum+candidates[i], i, path+[candidates[i]])

    dfs(0, 0, [])
    return result


print(comb_sum([2, 2, 3, 6, 7], 7))
