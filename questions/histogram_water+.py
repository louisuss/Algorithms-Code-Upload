# 최적화 해야함
def solution(histogram):
    answer = 0
    len_hist = len(histogram)
    for i in range(len_hist):
        if i+2 <= len_hist:
            for j in range(i+2, len_hist):
                water = (j-i-1) * min(histogram[i], histogram[j])
                answer = max(answer, water)
    return answer
