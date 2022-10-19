import math

def isPrimo(x):
    for i in (2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = 100
l = []

#l = [i for i in range(1, n) if isPrimo(i)]

for i in range(1, n):
    if isPrimo(i):
        l.append(i)

print(l)