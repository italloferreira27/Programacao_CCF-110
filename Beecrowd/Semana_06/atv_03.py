x = [0 for i in range(100)]
for i in range(100):
    x[i] = float(input())
for i in range(100):
    if(x[i] <= 10):
        print(f"A[{i}] = {x[i]}")