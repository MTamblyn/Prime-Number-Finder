import sys
integers = [k+1 for k in range(100)]
integers.remove(1)
for i in range (2,8):
    integers = list(filter(lambda x: x%i or x==i, integers))
    print ('removing multiples of', i)
    
print(integers)
print(sys.version)

