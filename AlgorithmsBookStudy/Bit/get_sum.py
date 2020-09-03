def get_sum(a, b):
    mask = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF
    # 합, 자릿수 처리
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    # 음수 처리
    if a > INT_MAX:
        a = ~(a ^ mask)
    return a
