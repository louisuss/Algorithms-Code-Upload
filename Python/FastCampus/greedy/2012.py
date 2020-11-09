# 예상등수 A , 실제등수 B, 불만도 = |A-B|
# 불만도 최소값 -> 학생등수매기기

# 1 5 3 1 2 -> sorting 1 1 2 3 5
# 1 2 3 4 5
n = int(input())
guess_rank = [int(input()) for _ in range(n)]
rank = [i for i in range(1, n+1)]

worst_score = 0
for a, b in zip(rank, sorted(guess_rank)):
    worst_score += abs(a - b)

print(worst_score)