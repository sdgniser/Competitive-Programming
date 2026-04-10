t = int(input())
for _ in range(t):
    n,m,l,r = list(map(int,input().split()))

    a = -min(abs(l),abs(m))
    m += a
    b = min(r,m)

    print(a,b)