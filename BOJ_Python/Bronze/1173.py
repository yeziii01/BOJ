N, m, M, T, R = map(int, input().split())   # 변수 연속으로 입력받기

now = m   # 현재 맥박과 초기 맥박 m으로 저장
exer_cnt = 0   # 운동한 시간(분)
cnt = 0   # 총 걸린 시간(분)

while True :
    if m + T > M:   # 운동을 N분 할 수 없을 때
        print("-1")   # -1 출력
        break   # 종료
    if exer_cnt == N :   # 운동한 시간이 N과 같을 떄
        print(cnt)   # 총 걸린 시간 출력
        break   # 종료
    if now < m :   # 현재 맥박이 m보다 작으면
        now = m   # 현재 맥박을 m으로 저장
    elif now == m :   # 현재 맥박이 m이면
        now = now + T   # 무조건 운동
        exer_cnt += 1   # 운동한 시간 증가
        cnt += 1   # 총 걸린 시간 증가
    elif now > M - T :   # 현재 맥박에 운동을 했을 떄 M을 초과하면
        now = now - R   # 무조건 휴식
        cnt += 1   # 총 걸린 시간 증가
    else :   # 위에 모두 해당하지 않으면 최
        now = now + T
        exer_cnt += 1
        cnt += 1