# 0
# 0 0 1
# 001 0 011
# 0010011 0 0011011
def solution(n):
    dp = [[0], [0], [0, 0, 1]]

    def reverse_data(k):
        k.reverse()
        a = []
        for i in k:
            if i == 1:
                a.append(0)
            else:
                a.append(1)
        return a

    for i in range(3, n+1):
        dp.append(dp[i-1] + [0] + reverse_data(dp[i-1]))

    return dp[n]

# def solution(n):
#     fold = 0
#     arr = [fold]

#     for i in range(n - 1):
#         arr = arr + [fold] + [bit ^ 1 for bit in arr[::-1]]

#     return arr
