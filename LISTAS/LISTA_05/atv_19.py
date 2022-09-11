#EX. 19
i = 1
a = 5000000
b = 7000000
while(a < b):
  a = a + (a * 0.03)
  b = b + (b * 0.02)
  i = i + 1
print(f"Foram necessários {i} anos para a cidade A({a}) ultrapassar a cidade b({b})")