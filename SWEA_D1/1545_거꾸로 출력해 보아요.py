import sys
sys.stdin = open("1545_거꾸로 출력해 보아요.txt", "r")

T = int(input()) + 1
for i in range(T):
    T -= 1
    print(T, end=' ')