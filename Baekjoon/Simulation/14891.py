from collections import deque

gear_list = []

# gear_list[0], gear_list[1], gear_list[2], gear_list[3]
for _ in range(4):
    gear = ' '.join(input())
    gear_list.append(deque(map(int, gear.split())))

k = int(input())
options = []
for _ in range(k):
    options.append(list(map(int, input().split())))

def rotate(gear_list, option):
    selection = option[0]
    direction = option[1]
    present_gear = gear_list[selection-1]
    temp_direction = -direction

    rotation_check = []
    for i in range(1, 4):
        if gear_list[i - 1][2] != gear_list[i][6]:
            rotation_check.append(True)
        else:
            rotation_check.append(False)

    if selection == 1:
        for i in range(3):
            if rotation_check[i]:
                gear_list[i+1].rotate(temp_direction)
                temp_direction = -temp_direction
            else:
                break

    elif selection == 2:
        if rotation_check[0]:
            gear_list[0].rotate(temp_direction)

        for i in range(1,3):
            if rotation_check[i]:
                gear_list[i+1].rotate(temp_direction)
                temp_direction = -temp_direction
            else:
                break

    elif selection == 3:
        if rotation_check[2]:
            gear_list[3].rotate(temp_direction)

        for i in range(1,-1,-1):
            if rotation_check[i]:
                gear_list[i].rotate(temp_direction)
                temp_direction = -temp_direction
            else:
                break
    else:
        for i in range(2,-1,-1):
            if rotation_check[i]:
                gear_list[i].rotate(temp_direction)
                temp_direction = -temp_direction
            else:
                break

    if direction == 1:
        present_gear.rotate(direction)
    else:
        present_gear.rotate(direction)


def score(number):
    if gear_list[number][0] == 1:
        if number == 0:
            return 1
        elif number == 1:
            return 2
        elif number == 2:
            return 4
        else:
            return 8
    else:
        return 0

for option in options:
    rotate(gear_list, option)


sum = 0
for i in range(4):
    sum += score(i)
print(sum)