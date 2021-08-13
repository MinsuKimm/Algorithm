import sys
sys.stdin = open("2058_자릿수 더하기.txt", "r")

a = list(map(int,input()))
print(sum(a))