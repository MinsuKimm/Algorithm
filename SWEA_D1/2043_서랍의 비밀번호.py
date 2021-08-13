import sys
sys.stdin = open("2043_서랍의 비밀번호.txt", "r")

a, b = list(map(int,input().split()))
print(a -b + 1)