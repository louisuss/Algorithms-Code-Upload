
a, b = map(int, input().split())

# 소수점 첫번째까지만 표시하는 경우가 발생
res = str(a/b)

# 정수부분, 소수점부분
int_side, decimal_side = res.split('.')
# 소수점 길이 = 1 -> 원하는 길이만큼 0 추가
if len(decimal_side) == 1:
    decimal_side += "0"
else:
    decimal_side = decimal_side[0:2]

res = int_side + '.' + decimal_side
print(res)