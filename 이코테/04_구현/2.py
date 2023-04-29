# 게임 개발 (p.118)

N, M = map(int, input().split())
x, y, dir = map(int, input().split())

visited = [[0] * M for i in range(N)]
map_ = []
for i in range(N):
  row = list(map(int, input().split()))
  map_.append(row)

# print(map_)
result = 1
# 북, 동, 남, 서 방향 
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

trials = 0
visited[x][y] = 1

while True:
  dir = (dir + 3) % 4
  dx, dy = delta[dir]
  nx = x + dx
  ny = y + dy
  # checking left side
  if map_[nx][ny] == 0 and visited[nx][ny] == 0:
    visited[nx][ny] = 1
    dir = (dir + 3) % 4 # turn left
    x = nx
    y = ny
    result += 1
    trials = 0
    continue
  else:
    trials += 1
    if trials == 4:
      # step back
      dx, dy = delta[dir]
      nx = x - dx
      ny = y - dy
      if map_[nx][ny] == 1:
        break
      x = nx
      y = ny
      trials = 0

print(result)