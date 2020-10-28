# 가로:W / 세로:H
# 대각선으로 잘랐을 때 생기는 직각삼각형에서의 정사각형 개수 구하기
import math


def solution(w, h):
    return (w*h) - (w+h-math.gcd(w, h))
