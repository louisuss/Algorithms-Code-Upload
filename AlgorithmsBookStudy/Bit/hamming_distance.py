def hamming_distance(x, y):
    return bin(x ^ y).count('1')

x = 1
y = 4

print(hamming_distance(x,y))