vt = [0 for i in range(5)]#15
vt2 = []
for i in range(5):#15
    vt[i] = int(input())
for i in range(5):#15
    if(vt[i] >= 0):
        vt2.append(vt[i]**0.5)
    else:
        vt2.append(-1)
print(vt2)