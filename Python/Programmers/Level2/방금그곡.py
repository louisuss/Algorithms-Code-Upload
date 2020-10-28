def calculate_music_length(m):
    cnt = 0
    for i in m:
        if i == '#':
            cnt += 1
    return len(m)-cnt


def solution(m, musicinfos):
    answer = (0, "(None)")
    title = []
    info = []
    duration = []
    listen = calculate_music_length(m)

    for musicinfo in musicinfos:
        s, e, t, i = musicinfo.split(',')
        title.append(t)
        info.append(i)
        temp1 = list(map(int, s.split(':')))
        temp2 = list(map(int, e.split(':')))
        # 재생 시간
        d = (temp2[0]-temp1[0])*60 + (temp2[1] - temp1[1])
        duration.append(d)

    for idx in range(len(musicinfos)):
        i = info[idx]
        d = duration[idx]

        # 들은 시간이 음악 길이보다 긴 경우 패스
        if listen > d:
            continue

        # 음악정보를 길이만큼 늘려야됨
        temp = i * (d // len(i)) + i[0:d % len(i)]
        # 늘린 정보로와 m 비교
        # 일치하는 부분이 존재할 경우 음악 길이, 제목 정답 입력
        print(temp)

        if m + '#' not in temp and m in temp:
            if answer[0] < d:
                answer = (d, title[idx])

    return answer[1]
