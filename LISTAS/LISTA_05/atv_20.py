#EX. 20 
s = 0
da = 1
db = 2
ca = 10
cb = 15
while(da != db):
  if(s == 0):
    da = 2000
    db = 0
  da = da - 10
  db = db + cb
  s = s + 1
  #print(f"da= {da} db= {db} em {s}")
print(f"Os ciclistas se encontraram no ponto {da}. \nO ciclista A percoreu {ca*s} metros. \nO ciclista B percoreu {cb*s} metros.")