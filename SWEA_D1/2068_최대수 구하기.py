import sys
sys.stdin = open("2068_최대수 구하기.txt", "r")
T = int(input())

for tc in range(1, T+1):
    a = list(map(int, input().split()))
    answer = 0
    for i in range(len(a)):
        if a[i] > answer:
            answer = a[i]
    print("#%d %d" % (tc, answer))