# 문자열 뒤집기(p.313)

s = input()
start = s[0]

result = 0

for i in range(len(s) - 1):
    if(s[i] != s[i + 1]):
        result += 1
if(s[-1] != start):
    result += 1

print(result // 2)