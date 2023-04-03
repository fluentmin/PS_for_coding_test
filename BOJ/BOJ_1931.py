n = int(input())
times = []
for _ in range(n):
  start, end = map(int, input().split())
  times.append((start, end))

times.sort(key=lambda x:x[1])

# print(times)
result = 0
current_end = 0
for time in times:
  if(current_end <= time[0]):
    result += 1
    current_end = time[1]

print(result)