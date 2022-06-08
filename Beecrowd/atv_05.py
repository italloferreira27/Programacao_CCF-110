ini = int(input())
fib = [0, 1]
for i in range(ini):
  quant = int(input())
  for i in range(2, quant+1):
    fib.append(fib[i-1] + fib[i-2])
  print(f"Fib({quant}) = {fib[quant]}")
  for i in range(quant, 1, -1):
    fib.remove(fib[i])