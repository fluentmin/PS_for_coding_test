# 왕실의 나이트 (p.115)

def is_movable(position):
  return 1 <= position <= 8

data = input()
row = ord(data[0]) - ord('a') + 1
col = int(data[1])

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
# 아래와 같이 steps 변수 선언할 수도 있음
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for i in range(8):
  moved_row = row + dx[i]
  moved_col = col + dy[i]
  if(is_movable(moved_row) and is_movable(moved_col)):
    result += 1

print(result)
    