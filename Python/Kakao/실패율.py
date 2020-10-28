def solution(N, stages):
    result = {}
    len_sg = len(stages)
    for stage in range(1, N+1):
        if len_sg:
            cnt = stages.count(stage)
            result[stage] = cnt / len_sg
            len_sg -= cnt
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)
