s, n = map(int, input().split())
n = str(n)
col, row = 2*s+3, s+2
w = '-'*s

u = '  ' + w + ' '
ll = ' ' + '|' + (' ' * s) + '|'
r = ' ' * (s+2) + '|'
l = ' ' + '|' + ' ' * (s+1)
e = ' ' * (s+2+1)
m = col//s

def one():
    global lcd
    for i in range(col):
        if i == 0:
            lcd[i]+= ' ' * (s+2)
        elif 0 < i < m:
            lcd[i]+=' ' * (s+1) + '|'
        elif i == m:
            lcd[i]+=' ' * (s+2)
        elif m < i < (col-1):
            lcd[i]+=' ' * (s+1) + '|'
        else:
            lcd[i]+=' ' * (s+2)

def two():
    global lcd
    for i in range(col):
        if i == 0:
            lcd[i]+=u
        elif 0 < i < m:
            lcd[i]+=r
        elif i == m:
            lcd[i]+=u
        elif m < i < (col-1):
            lcd[i]+=l
        else:
            lcd[i]+=u

def three():
    global lcd
    for i in range(col):
        if i == 0:
            lcd[i]+=u
        elif 0 < i < m:
            lcd[i]+=r
        elif i == m:
            lcd[i]+=u
        elif m < i < (col-1):
            lcd[i]+=r
        else:
            lcd[i]+=u

def four():
    global lcd
    for i in range(col):
        if i == 0:
            lcd[i]+=e
        elif 0 < i < m:
            lcd[i]+=ll
        elif i == m:
            lcd[i]+=u
        elif m < i < (col-1):
            lcd[i]+=r
        else:
            lcd[i]+=e

def five():
    global lcd
    for i in range(col):
        if i == 0:
            lcd[i]+=u
        elif 0 < i < m:
            lcd[i]+=l
        elif i == m:
            lcd[i]+=u
        elif m < i < (col-1):
            lcd[i]+=r
        else:
            lcd[i]+=u

def six():
    global lcd
    for i in range(col):
        if i == 0:
            lcd[i]+=u
        elif 0 < i < m:
            lcd[i]+=l
        elif i == m:
            lcd[i]+=u
        elif m < i < (col-1):
            lcd[i]+=ll
        else:
            lcd[i]+=u

def seven():
    global lcd
    for i in range(col):
        if i == 0:
            lcd[i]+=u
        elif 0 < i < m:
            lcd[i]+=r
        elif i == m:
            lcd[i]+=e
        elif m < i < (col-1):
            lcd[i]+=r
        else:
            lcd[i]+=e

def eight():
    global lcd
    for i in range(col):
        if i == 0:
            lcd[i]+=u
        elif 0 < i < m:
            lcd[i]+=ll
        elif i == m:
            lcd[i]+=u
        elif m < i < (col-1):
            lcd[i]+=ll
        else:
            lcd[i]+=u

def nine():
    global lcd
    for i in range(col):
        if i == 0:
            lcd[i]+=u
        elif 0 < i < m:
            lcd[i]+=ll
        elif i == m:
            lcd[i]+=u
        elif m < i < (col-1):
            lcd[i]+=r
        else:
            lcd[i]+=u

def zero():
    global lcd
    for i in range(col):
        if i == 0:
            lcd[i]+=u
        elif 0 < i < m:
            lcd[i]+=ll
        elif i == m:
            lcd[i]+=e
        elif m < i < (col-1):
            lcd[i]+=ll
        else:
            lcd[i]+=u

lcd = ['']*col
func_dict = {
    '0': zero,
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine
}

for i in n:
    func_dict[i]()

for i in range(col):
    print(lcd[i])






