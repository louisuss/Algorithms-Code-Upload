def solution(brown, yellow):
    for v in range(1, yellow+1):
        if yellow % v == 0:
            l = yellow // v
            if l >= v:
                if (v+2)*(l+2) - yellow == brown:
                    return [l+2, v+2]
print(solution(24,24))