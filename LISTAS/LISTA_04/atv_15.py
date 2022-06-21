d = 0
f = 0
a,b,c,d1,e,f1,g,h,i,j = map(int, input().split(" "))
if (a >= 10 and a<=20):
  d += 1
else:
  f += 1
if (b >= 10 and b<=20):
  d += 1
else:
  f += 1
if (c >= 10 and c<=20):
  d += 1
else:
  f += 1
if (d1 >= 10 and d1<=20):
  d += 1
else:
  f += 1
if (e >= 10 and e<=20):
  d += 1
else:
  f += 1
if (f1 >= 10 and f1<=20):
  d += 1
else:
  f += 1
if (g >= 10 and g<=20):
  d += 1
else:
  f += 1
if (h >= 10 and h<=20):
  d += 1
else:
  f += 1
if (i >= 10 and i<=20):
  d += 1
else:
  f += 1
if (j >= 10 and j<=20):
  d += 1
else:
  f += 1
print('Dentro do intervalo:', d)
print('Fora do intervalo:',f)