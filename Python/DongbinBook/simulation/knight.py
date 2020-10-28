# ord, chr

position = input()
now_row = int(position[1])
now_col = (ord(position[0]) % ord('a')) + 1

dirs1 = [(1,2), (1,-2), (-1,2), (-1,-2)]
dirs2 = [(2,1),(2,-1),(-2,1),(-2,-1)]
dirs = dirs1 + dirs2
count = 0
for dir in dirs:
    r, c = dir
    nr, nc = now_row+r, now_col+c
    if 1<= nr <= 8 and 1 <= nc <= 8:
        count += 1

print(count)