import sys
sys.stdin = open("2072_홀수만더하기.txt", "r")
T = int(input())

for tc in range(1, T+1):
    list = map(int, input().split())
    answer = 0
    for i in list:
        if i%2 != 0:
            answer += i
         
    print("#%d %d" % (tc, answer))