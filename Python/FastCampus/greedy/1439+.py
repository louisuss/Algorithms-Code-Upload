# 뒤집기
# 코딩 테스트에 전구 불키기와 같이 많이 출제됨. 빈출 유형
# 최소 뒤집기 횟수 -> 숫자 압축 -> 0001100 -> 010

s = input()

# Solution 1
def compress_number(s):
    compressed = s[0]
    for i in range(1, len(s)):
        if s[i] != compressed[-1]:
            compressed += s[i]
    return compressed

compressed_number = compress_number(s)
cnt_0 = compressed_number.count('0')
cnt_1 = compressed_number.count('1')

if cnt_0 > cnt_1:
    print(cnt_1)
else:
    print(cnt_0)

# Solution 2

data = input()
make_0 = 0  # 전부 0으로 바꾸는 경우 1->0
make_1 = 0  # 전부 1로 바꾸는 경우 0->1

if data[0] == '1':
    make_0 += 1
else:
    make_1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우 1->0
        if data[i + 1] == '1':
            make_0 += 1
        # 다음 수에서 0으로 바뀌는 경우 0->1
        else:
            make_1 += 1

print(min(make_0, make_1))
