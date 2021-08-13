import sys
sys.stdin = open("2050_알파벳을 숫자로 변환.txt", "r")

T = list(input())
for tc in T:
    print(ord(tc)-64, end=" ")