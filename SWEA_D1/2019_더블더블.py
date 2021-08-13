import sys
sys.stdin = open("2019_더블더블.txt", "r")

T = int(input())
for tc in range(T+1):
    print(2**tc, end=" ")