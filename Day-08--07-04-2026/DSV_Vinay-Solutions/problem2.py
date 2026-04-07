import math
n = int(input())
cn = math.comb(n,(n//2))
total = cn * ((math.factorial((n//2)-1))**2)
print(total//2)