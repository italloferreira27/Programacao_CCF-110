a,b,c = map(float, input().split(" "))

if(a < b + c and b < a + c and c < a + b):
    per = a + b + c
    print('Perimetro = %.1f' %per)
else:
    tra = ((a+b)*c)/2
    print('Area = %.1f' %tra)