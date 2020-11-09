def comb(n, k):
    results = []

    def dfs(elements, start, k):
        # 종료 조건
        if k == 0:
            results.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n+1):
            elements.append(i)
            # 뽑힌 숫자를 제외하고 반복
            dfs(elements, i+1, k-1)
            elements.pop()

    dfs([], 1, k)
    return results


print(comb(4, 2))


def solutions(lst, k):
    result = []
    prev_lst = []

    def dfs(lst, k):
        if len(prev_lst) == k:
            result.append(prev_lst[:])
            return

        # permute와 달리 for 문 밖으로 나옴
        next_lst = lst[:]
        for val in lst:
            prev_lst.append(val)
            next_lst.remove(val)
            dfs(next_lst, k)
            prev_lst.pop()
    dfs(lst, k)

    return result


print(solutions(["a", "b", "c", "d"], 3))
