x = [0 for i in range(10)]
for i in range(10):
    x[i] = float(input())
for i in range(10):
    if(x[i]<=0):
        x[i] = 1
        print(f"X[{i}] = {x[i]:.0f}")
    else:
        print(f"X[{i}] = {x[i]:.0f}")