N = int(input())
A_i = list(map(int, input().split()))   # 리스트에 저장
B, C = map(int, input().split())

sum_num = 0

for i in A_i:
    if (i-B) < 0 :
        sum_num += 1
    elif (i-B)%C == 0 :
        sum_num += 1 + (i-B)//C
    else:
        sum_num += 1 + 1 + (i-B)//C

print(sum_num)