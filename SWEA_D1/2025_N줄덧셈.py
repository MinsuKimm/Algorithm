import sys
sys.stdin = open("2025_N줄덧셈.txt", "r")

T = int(input())
answer = 0
for i in range(1, T+1):
    answer += i
print(answer)
