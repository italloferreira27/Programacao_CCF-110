#EX. 05
ini = int(input())
fib = [0 for i in range(1000)]
fib[0] = 0
fib[1] = 1
for i in range(ini):
    quant = int(input())
    for i in range(2, quant+1):
        fib[i] = fib[i-1] + fib[i-2]
    print(f"Fib({quant}) = {fib[quant]}")