# 설탕 배달

data = int(input())

result = 0

while(data > 0 and data % 5 != 0):
  data -= 3
  result += 1

result += data // 5
if(data < 0):
  result = -1

print(result)