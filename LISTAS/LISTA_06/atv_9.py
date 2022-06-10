vt = []
vt2 = []
vt3 = []
for i in range(5):
    vt.append(int(input("Digite um valor: ")))
for i in range(5):
    vt2.append(int(input("Digite um 2º valor: ")))
for i in range(5):
    vt3.append(vt[i] + vt2[i])
print(vt3)
