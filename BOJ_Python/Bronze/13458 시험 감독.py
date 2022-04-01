N = int(input())
A_i = list(map(int, input().split()))   # 리스트에 저장
B, C = map(int, input().split())   # B, C map으로 입력받기

sum_num = 0   # 감독관의 총 수

for i in A_i:   # 리스트를 반복문으로 돌림
    if (i-B) < 0 :   # i<B 이면 무조건 총감독관 1명만 필요
        sum_num += 1
    elif (i-B)%C == 0 :   # (i-B)가 C로 나눠떨어지면 총감독관 1명 + 몫
        sum_num += 1 + (i-B)//C
    else:   # (i-B)가 C로 나눠떨어지지 않으면 총감독관 1명 + 몫 + ㅂ감1관 1명 더
        sum_num += 1 + 1 + (i-B)//C

print(sum_num)