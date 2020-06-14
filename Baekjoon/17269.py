n, m = map(int, input().split())
a, b = input().split()

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

ab = ''
min_len = min(n, m)
for i in range(min_len):
    ab += a[i] + b[i]

ab += a[min_len:] + b[min_len:]

lst = [alp[ord(i)-ord('A')] for i in ab]

# 한번할때마다 길이가 1씩 줄어듬 2빼면 길이가 2만큼 남음
for i in range(n+m-2):
    # 각각의 길이
    # 앞으로 밀어준다고 생각
    for j in range(n+m-1-i):
        lst[j] += lst[j+1]

print('{}%'.format(lst[0]%10*10 + lst[1]%10))