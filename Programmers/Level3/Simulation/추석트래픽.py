def solution(lines):
    S, E = [], []
    total_lines = 0
    for line in lines:
        total_lines += 1
        d, s, t = line.split(' ')

        t = float(t[:-1])
        hh, mm, ss = s.split(':')
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)

        E.append(seconds + 1)
        S.append(seconds - t + 0.001)

    S.sort()

    cur_traffic = 0
    max_traffic = 0
    cnt_E = 0
    cnt_S = 0
    while ((cnt_E < total_lines) and (cnt_S < total_lines)):
        if(S[cnt_S]) < E[cnt_E]:
            cur_traffic += 1
            max_traffic = max(max_traffic, cur_traffic)
            cnt_S += 1
        else:
            cur_traffic -= 1
            cnt_E += 1
    return max_traffic
