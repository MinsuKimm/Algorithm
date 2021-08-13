import sys
sys.stdin = open("2071_평균값구하기.txt", "r")
T = int(input())

for tc in range(1, T+1):
    A = list(map(int, input().split()))
    answer = 0
    for i in A:
        answer += i

    print("#{} {}".format(tc, round(answer/len(A))))