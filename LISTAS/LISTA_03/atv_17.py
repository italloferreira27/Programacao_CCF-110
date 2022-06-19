#https://www.tutorialspoint.com/python3/python_multithreading.htm
#https://docs.python.org/3/library/threading.html#lock-objects
#https://vaiprogramar.com/como-usar-os-lacos-de-repeticao-for-e-while-em-python/
import itertools
a = 0
for i,j in itertools.product(range(1,100,2), range(1,51)):
  a = a + i/j
 # print(i,' ', j)
print(a)  
#for i,j in range(1, 100,2), range(51):
  #for j in range(51):
    #print(i)
    #a = a + i/j