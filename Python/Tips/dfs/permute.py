def permute(nums):
    results = []
    prev_elem = []

    def dfs(elements):
        # 종료 조건
        if len(elements) == 0:
            results.append(prev_elem[:])
            return

        for e in elements:
            next_elem = elements[:]
            # e = 뽑힌 원소
            # 뽑힌 원소 삭제한 리스트
            next_elem.remove(e)

            # 뽑힌 원소 추가
            prev_elem.append(e)
            # 뽑힌 원소 제외하고 뽑힐 수 있는 숫자로 다음 반복
            dfs(next_elem)
            # 호출 횟수만큼 pop 됨
            prev_elem.pop()
    dfs(nums)
    return results


nums = [1, 2, 3]
print(permute(nums))


def solutions(lst, k):
    result = []
    prev_lst = []

    def dfs(lst, k):
        if len(prev_lst) == k:
            result.append(prev_lst[:])
            return

        for val in lst:
            prev_lst.append(val)
            next_lst = lst[:]
            next_lst.remove(val)
            dfs(next_lst, k)
            prev_lst.pop()
    dfs(lst, k)

    return result


print(solutions([1, 2, 3], 3))
