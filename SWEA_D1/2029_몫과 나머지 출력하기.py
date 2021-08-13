import sys
sys.stdin = open("2029_몫과 나머지 출력하기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    a, b = list(map(int,input().split()))
    c = a // b
    d = a % b
    print("#{} {} {}" .format(tc, c, d))