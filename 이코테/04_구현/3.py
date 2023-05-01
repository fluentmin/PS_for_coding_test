# 럭키 스트레이트 (p.321)

N = input()
l = len(N)

pointer_1 = 0
pointer_2 = l // 2

sum_1 = 0
sum_2 = 0

for i in range(l // 2):
  sum_1 += int(N[pointer_1])
  sum_2 += int(N[pointer_2])
  pointer_1 += 1
  pointer_2 += 1

if(sum_1 == sum_2):
  print("LUCKY")
else:
  print("READY")