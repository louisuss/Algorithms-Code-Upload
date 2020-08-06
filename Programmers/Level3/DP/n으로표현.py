# +, -, * , //
# 오답
# +, -, * , //
# 오답

# def solution(N, number):
#     answer = 1
#     dp = [[5]]
#     if number == dp[0][0]:
#         return 1
#     while answer <= 8:
#         temp = []
#         # 이전 dp 값
#         temp.append(int(str(N)*(answer+1)))
#         for v in dp[answer-1]:
#             temp.append(v+N)
#             temp.append(v-N)
#             temp.append(N-v)
#             temp.append(v*N)
#             if v//N > number:
#                 continue
#             else:
#                 temp.append(v//N)
#         answer += 1
#         if number in temp:
#             return answer
#         dp.append(temp)
#     return -1


def solution(N, number):
    possible_set = [0, [N]]  # 조합으로 나올수 있는 가능한 숫자들, 여기에 계속 append하며 이후에 사용함
    if N == number:  # 주어진 숫자와 사용해야 하는 숫자가 같은 경우는 1개면 족하므로 1으로 놓는다.
        return 1
    for i in range(2, 9):  # 2부터 8까지로 횟수를 늘려 간다.
        case_set = []  # 임시로 사용할 케이스 셋, 각 I 별로 셋을 만들어 possible set에 붙인다.
        basic_num = int(str(N)*i)  # 같은 숫자 반복되는 거 하나를 추가한다.
        case_set.append(basic_num)
        # 사용되는 숫자의 횟수를 구해야 하는데, 절반 이상으로 넘어가면 같은 결과만 나올 뿐이므로 절반까지만을 사용한다.
        # 2,3,4,5,6,7,8
        # (1,2),(1,2),(1,3),(1,3),(1,4),(1,4),(1,5)
        for i_half in range(1, i//2+1):
            # dp[3] = dp[1]+dp[2], dp[4] = dp[1]+dp[3], dp[2]+dp[2]
            for x in possible_set[i_half]:
                for y in possible_set[i-i_half]:  # x와 y를 더하면 i 가 되도록 만든 수다.
                    print(possible_set)
                    case_set.append(x+y)  # 각 사칙연산 결과를 더한다.
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y != 0:
                        case_set.append(x/y)
                    if x != 0:
                        case_set.append(y/x)
            if number in case_set:
                return i
            possible_set.append(case_set)  # 최종 결과물 set에 사칙 연산 결과를 더한다.
    return -1  # N 이 8까지 답이 없으면 -1을 출력한다.
