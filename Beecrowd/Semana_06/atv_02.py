x = [0 for i in range(10)]
v = int(input())
for i in range(10):
    if(i == 0):
        x[i] = v
        print(f"N[{i}] = {x[i]}")
    else:
        x[i] = x[i-1] * 2
        print(f"N[{i}] = {x[i]}")