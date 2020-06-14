bird = int(input())
cnt = 0
sing_num = 1

while bird > 0:
    if sing_num <= bird:
        bird = bird - sing_num
        sing_num += 1
        cnt += 1
    else:
        sing_num = 1

print(cnt)