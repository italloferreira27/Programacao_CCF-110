#https://www.delftstack.com/pt/howto/python/fibonacci-sequence-python/#:~:text=Copy%200%2C1%2C1%2C,s%C3%A3o%200%20e%201%2C%20respectivamente.
n1 = 1
n2 = 1
for i in range(20):
  print(n1)
  aux = n1
  n1 = aux
  n1 = n2
  n2 = aux + n2