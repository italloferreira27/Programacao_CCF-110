v = float(input("Digite o valor da aula: "))
a = float(input("Digite o números de aulas: "))
d = float(input("Digite o valor em porcentagem do desconto do INSS: "))
dd = d/100
vl = (a*v)*dd
print("Valor líquido é de: ", vl)
