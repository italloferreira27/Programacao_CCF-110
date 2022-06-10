vt = []
media = 0
mm = 0
i = 0
for i in range(10):#10
    vt.append(int(input()))
    media += vt
    i += 1
mm = media/i
for i in range(10):#10
    if(vt[i] > media):
        print(vt[i])