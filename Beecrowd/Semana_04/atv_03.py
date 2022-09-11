#EX. 03
a,b,c = map(int, input().split(" "))
if (a >= -100 and a <= 100 and b >= -100 and b <= 100 and c >= -100 and c <= 100):
  if (a > b and b <= c):
    print(':)')
  elif(a < b and b >= c):
    print(':(')
  elif(a < b and b < c and (c-b) < (b-a)):
    print(':(')
  elif(a < b and b < c and (c-b) >= (b-a)):
    print(':)')
  elif (a > b and b > c and (b-c) < (a-b)):
    print(':)')
  elif (a > b and b > c and (b-c) >= (a-b)):
    print(':(')
  elif (a == b and b < c):
    print(':)')
  elif (a == b and b >= c):
    print(':(')