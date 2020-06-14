morning,night,tree = map(int, input().split())
move = morning - night

if (tree - night) % move != 0:
    print((tree-night)//move + 1)
else:
    print((tree-night)//move)
