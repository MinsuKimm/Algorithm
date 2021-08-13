import sys
sys.stdin = open("1933_간단한 N의 약수.txt", "r")

N = int(input())
for tc in range(1,N+1):
    if N % tc ==0:
        print(tc, end= " ")