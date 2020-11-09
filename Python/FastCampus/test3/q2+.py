import sys
sys.setrecursionlimit(int(1e7))






n, m, h = map(int, input().split())

pick = 0
# 메모리 초과
def solution1():
    def dfs(cases, idx):
        global pick
        if sum(cases) == h:
            pick += 1
            print(cases)
            return
        elif sum(cases) > h:
            return

        if idx == n:
            return

        for case in students[idx]:
            cases.append(case)

            dfs(cases, idx+1)
            cases.pop()  # 호출 횟수만큼 pop
    students = [[0]+list(map(int, input().split())) for _ in range(m)]
    dfs([], 0)
    print(pick % 10007)

def solution2():
    students = [list(map(int,input().split())) for _ in range(n)]
    dp = [0]*(h+1) # 누적 높이
    dp[0] = 1

    # i: 학생
    for i in range(n):
        data = []
        # j: 0 ~ h까지 모든 높이에 대해 처리
        for j in range(h+1):
            # k: 학생 블록
            for k in range(len(students[i])):
                # j 높이 쌓인적 있고 현재 학생의 블록 + 이전 블록의 높이
                if dp[j] != 0 and j + students[i][k] <= h:
                    data.append((j+students[i][k], dp[j]))
        # 쌓을 수 있는 높이에 대해 경우의 수 증가
        for height, value in data:
            dp[height] = (dp[height] + value) % 10007
    print(dp[h])

solution2()

