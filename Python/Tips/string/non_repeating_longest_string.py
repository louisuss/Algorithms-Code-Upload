
# 슬라이딩 윈도우(윈도우를 한칸씩 이동) + 투포인터 사이즈 조절
# 슬라이딩 윈도우로 한 칸씩 우측 이동 -> 윈도우 내에 모든 문자가 중복 없도록 투 포인터로 윈도우 사이즈 조절

def longest_string(s):
    used = {}
    max_length = start = 0

    # 투 포인터 (start, idx)
    for idx, char in enumerate(s):
        # 이미 등장했던 문자면 start 위치 갱신
        # 현재 슬라이딩 윈도우의 바깥에 있는 문자는 예전에 등장한 적이 있더라도 지금은 무시 *
        if char in used and start <= used[char]:
            start = used[char] + 1
        else: # 최대 부분 문자열 갱신
            max_length = max(max_length, idx-start+1)
        
        # 현재 문자의 위치 삽입
        used[char] = idx
    
    return max_length