# nlog(n)
def get_distance(local_idx):
    result = 0
    for antena in antenas:
        result += abs(antena - antenas[local_idx])
    return result


# 4 -> 2, 5 -> 2
n = int(input())
antenas = sorted(map(int, input().split()))

len_antenas = len(antenas)
idx = len_antenas // 2
answer = 0
# 짝수
if len_antenas % 2 == 0:
    a = get_distance(idx-1)
    b = get_distance(idx)
    if a >= b:
        answer = antenas[idx-1]
    else:
        answer = antenas[idx]
# 홀수
else:
    answer = antenas[idx]

print(answer)
