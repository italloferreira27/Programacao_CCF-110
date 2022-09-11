a,b,c,d = map(int, input().split(" "))

ss = c + d
s = a + b
par = a%2

if(b > c and d > a and ss > s and c>0 and d>0 and par==0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')