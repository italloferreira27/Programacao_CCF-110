a,b = map(float, input("Digite a hora (hh:mm): ").split(":"))
if(a < 24 and b < 60):
    vh = a*60
    print("Já passou das 0:00: ", vh+b, "minutos.")
else:
    print("Inválido!")