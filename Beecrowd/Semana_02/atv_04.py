a,b = map(int, input(). split(" "))

if(a >= b):
    h = (24 - a) + b
    print("O JOGO DUROU", h, "HORA(S)")
else:
    h = b - a
    print("O JOGO DUROU", h, "HORA(S)")