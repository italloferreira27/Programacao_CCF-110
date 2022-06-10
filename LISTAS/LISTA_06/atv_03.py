vt = []
troca = 0
for i in range(20):
    vt.append(int(input()))
for i in range(10):
    troca = vt[i]
    vt[i] = vt[19-i]
    vt[19-i] = troca
print(vt)