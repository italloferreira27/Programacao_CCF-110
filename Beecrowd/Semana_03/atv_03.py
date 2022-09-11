a = int(input())
b = int(input())
v = 0
if(a >= b):
    for i in range(b+1, a):
        if(i%2 != 0):
            v = v + i
else:
    for i in range(a+1, b):
        if(i%2 != 0):
            v = v + i
print(v)