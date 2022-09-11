#EX. 01
cont = 0
n = int(input())
for i in range(n):
  if(i <= 1):
    print(i, end=" ")
    a1 = i
    a2 = i-1
  if(i > 1 and i < n-1):
    cont = a1 + a2
    print(cont, end=" ")
    a2 = a1
    a1 = cont
  if(i == n-1):
    cont = a1 + a2
    print(cont)