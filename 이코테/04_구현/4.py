# 문자열 재정렬 (p.322)

data = input()

ans_str = ""
ans_int = 0

for char in data:
  if char.isalpha():
    ans_str += char
  else:
    ans_int += int(char)

print(''.join(sorted(ans_str)) + str(ans_int))