from collections import deque

n = input()
var_list = list(map(str, n.split(',')))

first_list = var_list[0].split(' ')
common = first_list[0]
last = var_list[-1][-1]
var_list[0] = ' ' + first_list[1]
var_list[-1] = var_list[-1][0:-1]

def func(var):
    var = list(var.split(' '))
    if len(var) == 1:
        var[0] = reversed(var[0])
        var[0] = common + var[0]
        var[0][-1] = ' ' + var[0][-1]

    else:
        temp = common+var_list[0]
        var[1] = reversed(var[1])


