# 숫자 카드 게임 (p.96)

n, m = map(int, input().split())

min_value = 0

for i in range(n):
  row_list = list(map(int, input().split()))
  min_tmp = min(row_list)
  # if(min_value < min_tmp):
  #   min_value = min_tmp
  # 위 방식 대신 아래처럼 간단히 할 수도
  min_value = max(min_value, min_tmp)
  
print(min_value)