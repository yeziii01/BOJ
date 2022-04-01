def two(num) :   # 2의 제곱수인지 아닌지 확인하는 함수
    i = 2
    else_num = 0   # num을 나눠줄 2 이외의 다른 수(존재 여부만 확인하면 됨)
    while num != 1 :
        if num%i != 0 :
            else_num += 1   # 2 이외의 다른 수를 나눠줘야 함
            break
        num /= i
    if else_num > 0 :   # 2의 제곱수가 아니면 1 return
        return 1
    else :   # 2의 제곱수이면 0 return
        return 0

while True :
    sum_game = 0   # 전체 게임수
    plus_team = 0   # 추가해야 하는 팀수
    G, T, A, D = map(int, input().split())
    if D == -1 :   # 종료 조건
        break
    sum_game += (T*(T-1))/2*G   # 리그

    tnmt_cnt = G*A+D   # 토너먼트에 참가하는 팀수
    result = two(tnmt_cnt)   # 함수 결과를 result에 저장

    tmp = 1   # ##1에 쓰이는 변수, 2의 제곱수로 cnt와 비교하는 데에 쓰임
    if result == 1 :   # 2의 제곱수가 아니면
        while True:   # 가까운 2의 제곱수로 만들어주는 과정(##1)
            if tmp > tnmt_cnt :
                plus_team = tmp-tnmt_cnt   # 차이만큼 plus_team에 저장
                tnmt_cnt = tmp   # 가장 가까운 2의 제곱수인 tmp를 tnmt_cnt에 저장
                break
            tmp *= 2

    while tnmt_cnt != 1 :   # 토너먼트
        tnmt_cnt /= 2
        sum_game += tnmt_cnt


    print(f"{G}*{A}/{T}+{D}={int(sum_game)}+{plus_team}")
