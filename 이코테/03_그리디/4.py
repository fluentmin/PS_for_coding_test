# 모험가 길드(p.311)

n = int(input())
data = list(map(int, input().split()))

data.sort()
result = 0
tmp = 1 # 현재 모인 모험가 수

for i in data:
  if(i <= tmp): # 그룹 만들기
    result += 1
    tmp = 1
  else:
    tmp += 1

print(result)