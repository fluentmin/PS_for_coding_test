# 볼링공 고르기(p.315)

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = 0
for i in range(n):
    tmp = i # pointer
    # 서로 다른 값이 나올 때까지 pointer 오른쪽으로 이동
    while(data[tmp] == data[i]):
        tmp += 1
        # indexing error 처리
        if(tmp == n):
            break

    result += n - tmp

print(result)