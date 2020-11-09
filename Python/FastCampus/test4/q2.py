from itertools import permutations

n, k = map(int, input().split())
exercise_kits = list(map(int, input().split()))


def solution1():
    result = []
    for case in permutations(exercise_kits, n):
        muscle = 500
        check = False
        for kit in case:
            muscle += kit
            muscle -= k
            if muscle < 500:
                check = True
                break
        if not check:
            result.append(case)
    return len(result)


print(solution1())

# 에러


def solution2(n, k, exercise_kits):
    result = []
    prev_kits = []

    def dfs(muscle, kits):
        if len(prev_kits) == n:
            result.append(prev_kits[:])
            return
        if muscle < 500:
            return

        for kit in kits:
            muscle += kit
            muscle -= k

            # return 문에 의해 함수 바로 종료
            # if muscle < 500:
            #     return

            # 다음 사용가능 키트 목록
            next_kits = kits[:]
            next_kits.remove(kit)
            # 사용한 키트 저장
            prev_kits.append(kit)
            dfs(muscle, next_kits)
            prev_kits.pop()
    dfs(500, exercise_kits)
    print(len(result))


solution2(n, k, exercise_kits)


# def dfs(muscle, case, start, kits):
#     muscle += start
#     muscle -= k
#     if muscle < 500:
#         return
#     if len(case) == n:
#         result.append(case)
#         return
#     kits.remove(start)
#     case.append(start)
#     print(case)
#     for kit in kits:
#         dfs(muscle, case, kit, kits)
#         kits.append(start)

# for kit in exercise_kits:
#     dfs(500, [], kit, exercise_kits)
