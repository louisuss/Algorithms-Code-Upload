# 구하는 카드 합
num = int(input())
cnt = int(input())
cards = list(map(int, input().split()))

def solution(num, cards):
    dp = [0] * (num+1)
    dp_start = cards[0]

    #  dp[card] : 값을 위한 최소 카드 필요 개수
    for card in range(dp_start, num+1):
        if card in cards:
            dp[card] = 1
            continue
        
        for i in range(card-1, 0, -1):
            temp = 1000
            if dp[i] and dp[card-i]:
                dp[card] = min(temp, dp[i]+dp[card-i])

    return dp[num] if dp[num] else -1


print(solution(num, cards))
