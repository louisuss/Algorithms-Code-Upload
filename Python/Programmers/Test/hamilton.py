from collections import defaultdict

t = [[5, 1], [2, 5], [3, 5], [3, 6], [2, 4], [4, 0]]


def solution(t):
    def dfs(start):
        visited[start] = True

        for next in tree[start]:
            if not visited[next]:
                visited_cnt[next] += 1
                dfs(next)
                if visited_cnt[start] == 2:
                    return
                if visited.count(True) != len(t)+1:
                    visited_cnt[start] += 1  # 위치 복귀

    answer = 0

    tree = defaultdict(list)
    for a, b in t:
        tree[a].append(b)
        tree[b].append(a)

    answer = 0
    for i in range(len(t)+1):
        visited_cnt = [0]*(len(t)+1)
        visited = [False]*(len(t)+1)
        dfs(i)
        cnt = 0
        for n in visited_cnt:
            if n != 0:
                cnt += 1

        answer = max(answer, cnt)

    return answer


print(solution(t))
