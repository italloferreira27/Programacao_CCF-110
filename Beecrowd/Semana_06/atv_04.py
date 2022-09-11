x = [0 for i in range(20)]
cont = 0
for i in range(20):
    x[i] = int(input())
for i in range(10):
    cont = x[i]
    x[i] = x[19-i]
    x[19-i] = cont
    #x[i] = cont[i]
    #x[4] = x[4-1]
for i in range(20):
    print(f"N[{i}] = {x[i]}")