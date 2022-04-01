year1, month1, day1 = map(int, input().split())
year2, month2, day2 = map(int, input().split())

day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   # 평년일 때 한 달의 일수

sum_1 = 0   #
sum_2 = 0   #

def year(year):
    sum = 0
    for i in range(1, year):
        if (i%4==0 and i%100!=0) or (i%400==0):
            sum += 366
        else:
            sum += 365
    return sum

sum_1 += year(year1)
sum_2 += year(year2)

for i in range(month1-1):
    if (year1 % 4 == 0 and year1 % 100 != 0) or year2 % 400 == 0:
        day_month[1] = 29
    sum_1 += day_month[i]

for i in range(month2-1):
    if (year2 % 4 == 0 and year2 % 100 != 0) or year2 % 400 == 0:
        day_month[1] = 29
    sum_2 += day_month[i]

sum_1 += day1
sum_2 += day2

remaining_days = sum_2 - sum_1

if (year2 == year1+1000 and month2 >= month1 and day2 >= day1) or year2 > year1+1000:
    print("gg")
else:
    print(f"D-{remaining_days}")