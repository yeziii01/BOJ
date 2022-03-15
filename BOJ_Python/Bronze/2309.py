height = []  # 난쟁이들의 키를 닮을 리스트

for i in range(9):  # for 반복문으로 난쟁이의 키 입력
    h = int(input())
    height.append(h)

sum_h = 0  # 난쟁이들의 키의 합 초기 0으로 설정
a = 0  # 밑에 반복문을 끝내주기 위한 수단

for i in height:  # for 반복문으로 난쟁이들의 키의 합
    sum_h += i

di = sum_h - 100  # 난쟁이들의 키의 합과 100의 차이

for i in range(0, 8):  # 이중 for문으로
    for j in range(i + 1, 9):
        if height[i] + height[j] == di:
            del height[i]
            del height[j - 1]
            height.sort()
            a = 1
            for k in height:
                print(k)
            break
    if a == 1:
        break


