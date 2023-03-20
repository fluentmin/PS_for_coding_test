# 동전 0

n, k = map(int, input().split())
data = []
for i in range(n):
  data.append(int(input()))

data.sort(reverse=True)

result = 0
for coin in data:
  if(k != 0):
    result += k // coin
    k %= coin

print(result)