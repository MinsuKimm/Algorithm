import sys
sys.stdin = open("1938_아주 간단한 계산기.txt", "r")

a, b = list(map(int, input().split()))
print(a + b)
print(a - b)
print(a * b)
print(a // b)