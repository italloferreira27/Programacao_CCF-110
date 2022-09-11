#EX. 04
pa, pg, ra, rg = map(float, input().split(" "))
aa = ra / pa
gg = rg / pg
if (aa > gg):
  print('A')
else:
  print('G')