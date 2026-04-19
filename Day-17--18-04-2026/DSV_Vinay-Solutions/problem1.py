t = int(input())

import math

def solve():
    n = int(input())
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i == 0:
            print(n//i,n-(n//i))
            return 1
    print(1,n-1)

for _ in range(t):
    solve()