
# 투 포인터 활용
def reverse_string(s):
    left, right = 0, len(s)-1
    
    while left < right:
        s[left], s[right] = s[right], s[left] # SWAP
        left += 1
        right -= 1

# Pythonic Way
def reverse_string2(s):
    s.reverse()
