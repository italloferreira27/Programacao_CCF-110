s = 0
a = 0
x = int(input())
for i in range(25, 0, -1):
  a += 1
  s += (((x**i)/a) * (-1)**(i+1))
print(s)