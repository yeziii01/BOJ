height = []  # 난쟁이들의 키를 닮을 리스트

for i in range(9):  # for 반복문으로 난쟁이의 키 입력
    h = int(input())
    height.append(h)

sum_h = 0  # 난쟁이들의 키의 합 초기 0으로 설정
a = 0  # 밑에 반복문을 끝내주기 위한 수단

for i in height:  # for 반복문으로 난쟁이들의 키의 합
    sum_h += i

di = sum_h - 100  # 난쟁이들의 키의 합과 100의 차이

for i in range(0, 8):  # 이중 for문으로 각각 8, 7번 반복해서 돌려줌
    for j in range(i + 1, 9):
        if height[i] + height[j] == di:   # 두 난쟁이의 키의 합이 차이와 같으면
            del height[i]   # 그 난쟁이의 키 리스트에서 제거
            del height[j - 1]   # 앞에 있는 height[i] 먼저 삭제했기 때문에 리스트 인덱스가 앞당겨짐
            height.sort()   # 리스트 오름차순으로 정렬
            a = 1   # 반복문이 끝남을 알림
            for k in height:   # 리스트에 있는 값들 모두 출력
                print(k)
            break
    if a == 1:   # for 반복문 모두 종료
        break


