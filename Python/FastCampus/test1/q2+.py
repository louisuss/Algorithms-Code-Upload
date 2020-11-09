n, k = map(int,input().split())
number_list = sorted(map(int, input().split()), reverse = True)
result = 0

def solution1():
    def dfs(x):
        global result
        if x > n:
            return
        # k의 원소로만 구성된 가장 큰 수를 저장
        result = max(x, result)
        for number in number_list:
            # k의 원소로만 구성된 모든 수를 탐색
            dfs(x*10 + number)
    dfs(0)
    print(result)
solution1()


# n, k = input().split()
# number_list = sorted(map(int, input().split()), reverse=True)

# def solution2():
#     answer = ""
#     check = False
#     for number in n:
#         number = int(number)
#         for l in number_list:
#             if not check:
#                 if number == l:
#                     answer += str(l)
#                     break
#                 if number > l:
#                     check = True
#                     answer += str(l)
#                     break
#             else:
#                 answer += str(l)
#                 break

#     print(int(answer))
