s = 0
for i in range(1, 52, 1):
  s +=((-1)**(i+1)) * 1/((2*i-1)**3)  
  pi = ((s) * 32) ** (1/3)
  #print(i)
print(pi)