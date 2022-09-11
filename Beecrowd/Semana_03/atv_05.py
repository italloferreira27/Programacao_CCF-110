def infinity():
    i=0
    while True:
        i+=1
        yield i

for i in infinity():
    sm = 0  
    m, n = map(int, input().split(" "))
    if(m > 0 and n > 0):
      if(m > n):
        for i in range(n, m+1):
            sm = sm + i
            print(i, end=" ")
            #continue
            #print(f"sum={sm}")
        print(f"Sum={sm}") 
      else:
        for i in range(m, n+1):
            sm = sm + i
            print(i, end=" ")
            #continue
            #print(f"sum={sm}")
        print(f"Sum={sm}")            
    else:
        break