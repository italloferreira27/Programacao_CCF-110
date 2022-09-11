a = float(input("Digite o valor da compra: "))
if(a < 10):
    print("Valor do lucro: ", a*0.7)
elif(a >= 10 and a < 30):
    print("Valor do lucro: ", a*0.5)
elif(a >= 30 and a < 50):
    print("Valor do lucro:", a*0.4)
elif(a >= 50):
    print("Valor do lucro: ", a*0.3)