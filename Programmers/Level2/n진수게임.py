DIGITS = [str(i) for i in range(10)] + [chr(i)
                                        for i in range(ord('A'), ord('G'))]


def conv(n, base):
    if n == 0:
        return DIGITS[0]

    digits = []
    while n > 0:
        digits.append(DIGITS[n % base])
        n = int(n//base)

    return ''.join(digits[::-1])


def solution(n, t, m, p):
    digits = []
    turn = 0
    while len(digits) < t*m:
        digits += list(conv(turn, n))
        turn += 1
    return ''.join(digits[p-1::m][:t])
