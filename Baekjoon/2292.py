room = int(input())
if room == 1:
    print(1)
else:
    idx = 1
    count = 1
    while True:
        if idx < room:
            idx = idx + 6 * count
            count += 1
        else:
            break
    print(count)