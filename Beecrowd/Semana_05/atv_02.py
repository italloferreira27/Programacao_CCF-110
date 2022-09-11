s2 = 3
s1 = 2
conts1 = 0
s = 1
for i in range(1, 20):
  s += s2/s1
  conts1 = s1
  s1 = conts1 * 2
  s2 += 2
#print(s)
#print(f"{round(s, 2)}")
print('%.2f' %s)