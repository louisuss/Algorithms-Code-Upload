result = []
candidates = list(map(int, input().split()))
target = int(input())


def dfs(csum, idx, path):
    if csum < 0:
        return
    if csum == 0:
        result.append(path)
        return
    for i in range(idx, len(candidates)):
        dfs(csum-candidates[i], i, path + [candidates[i]])


dfs(target, 0, [])
print(result)
