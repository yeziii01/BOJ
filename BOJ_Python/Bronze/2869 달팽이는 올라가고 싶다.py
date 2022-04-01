A, B, V = map(int, input().split())

now = 0
cnt = 0

while True:
    cnt += 1
    now += A
    if now >= V:
        break
    else:
        now -= B

print(cnt)
