s = input()

# 자릿수 == s의 문자
for i in range(9, -1, -1):
    for c in s:
        if int(c) == i:
            print(c, end="")
