vt = []
vt2 = []
for i in range(10):
    vt.append(int(input("Digite um valor: ")))
for i in range(5):
    vt2.append(vt[i] + vt[i+1])
print(vt2)
