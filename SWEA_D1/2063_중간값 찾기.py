import sys
sys.stdin = open("2063_중간값 찾기.txt", "r")
T = 1

for tc in range(1, T+1):
    N = int(input())
    a = sorted(list(map(int, input().split())))
    print(a[N//2])