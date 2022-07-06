n = int(input())
vt = []
cont = 0
nwvt = []
for i in range(n):
    vt.append(int(input()))

for i in range(n):
    for j in range(n):
        if(vt[i] == vt[j]):
            cont += 1
    nwvt.append([vt[i], cont])
    cont = 0

for i in range(n):
    for j in range(i+1, n):
        if(nwvt[i][0] == nwvt[j][0]):
            nwvt[j][0] = 0
vt = []
for i in range(n):
    if(nwvt[i][0] != 0):
        vt.append([nwvt[i][0], nwvt[i][1]])

for i in range(len(vt)):
    for j in range(i+1, len(vt)):
        if(vt[i] > vt[j]):
            vt[i], vt[j] = vt[j], vt[i]
            #troca = vt[i]
            #vt[i] = vt[j]
            #vt[j] = troca

for i in range(len(vt)):
    print(f'{vt[i][0]} aparece {vt[i][1]} vez(es)')