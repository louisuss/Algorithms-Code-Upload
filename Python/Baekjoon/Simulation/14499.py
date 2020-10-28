# n = row / m = column
n, m, x, y, k = map(int, input().split())
map_info = []
for _ in range(n):
    map_info.append(list(map(int, input().split())))

actions = list(map(int, input().split()))

# x = row / y= column
# east(1), west(2), north(3), south(4)
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

class Dice:
    def __init__(self, top=0, bottom=0, east=0, west=0, north=0, south=0):
        self.top = top
        self.bottom = bottom
        self.east = east
        self.west = west
        self.north = north
        self.south = south

def move(dice, direction):
    global x
    global y

    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        pass
    else:
        x = nx
        y = ny

        # east
        if direction == 1:
            dice.east, dice.bottom, dice.west, dice.top = dice.bottom, dice.west, dice.top, dice.east

        # west
        elif direction == 2:
            dice.top, dice.west, dice.bottom, dice.east = dice.west, dice.bottom, dice.east, dice.top

        # north
        elif direction == 3:
            dice.top, dice.south, dice.bottom, dice.north = dice.south, dice.bottom, dice.north, dice.top
        # south
        elif direction == 4:
            dice.top, dice.south, dice.bottom, dice.north = dice.north, dice.top, dice.south, dice.bottom


        if map_info[nx][ny] == 0:
            map_info[nx][ny] = dice.bottom
        else:
            dice.bottom = map_info[nx][ny]
            map_info[nx][ny] = 0

        print(dice.top)

dice = Dice()

for action in actions:
    move(dice, action)




