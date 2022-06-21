for i in range(1, 6):
  a, b = map(int, input().split(" "))
  for j in range(a, b+1):
    if(j%2==0):
      print(j)