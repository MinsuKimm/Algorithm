import sys
sys.stdin = open("2056_연월일 달력.txt", "r")

T = int(input())

for tc in range(1, T+1):
    Date = input()
    year = Date[0:4]
    month = Date[4:6]
    day = Date[6:8]
    if int(month) in (1, 3, 5, 7, 8, 10, 12):
        if int(day) <= 31:
           print("#{} {}/{}/{}".format(tc, year, month, day))
        else:
            print("#{} {}".format(tc, -1))
    elif int(month) in (4, 6, 9, 11):
        if int(day) <= 30:
           print("#{} {}/{}/{}".format(tc, year, month, day))
        else:
            print("#{} {}".format(tc, -1))
    elif int(month) ==2:
        if int(day) <=28:
            print("#{} {}/{}/{}".format(tc, year, month, day))
        else:
            print("#{} {}".format(tc, -1))
    else:
        print("#{} {}".format(tc, -1))