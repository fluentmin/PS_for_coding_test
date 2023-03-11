# 큰 수의 법칙 (p.92)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
max1 = data[0] # 가장 큰 값
max2 = data[1] # 두 번째로 큰 값

result = 0
for i in range(m):
  if(i % 4 == 3):
    result += max2
  else:
    result += max1

print(result)