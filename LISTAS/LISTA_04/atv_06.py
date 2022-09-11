v = float(input("Digite o valor do sálario mínimo: "))
ve = float(input("Digite os quilowatt: "))
vq = ve/100
vv = v/7
vt = vv*vq
vcq = vt/vq
d = vt - (vt*0.1)
print("valor de cada QuiloWatt: ", vcq)
print("Valor total a ser pago R$", vt)
print("Valor com 10/100 de desconto: ", d)