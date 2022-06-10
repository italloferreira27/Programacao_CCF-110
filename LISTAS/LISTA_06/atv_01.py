vt = [0 for i in range(30)]
a = int(input())
mult = 0
for i in range(30):
    vt[i] = int(input())
for r in range(30):
    mult = vt[r] * a
    if(mult%2==0):
        print(f"{mult} é par!")
    else:
        print(f"{mult} é ímpar!")