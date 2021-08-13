import sys
sys.stdin = open("2027_대각선 출력하기.txt", "r")

for i in range(5):
    for j in range(5):
        if i == j :
            print('#', end= "")
        else :
            print("+", end= "")
    print("")