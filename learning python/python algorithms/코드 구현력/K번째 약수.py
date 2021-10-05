n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n % 1 == 0:
        cnt+=1
    if cnt == k:
        print(i)
        break
# 정상적으로 끝났다면 else
else:
    print(-1)