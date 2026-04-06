t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    res = []
    a,b = n , 1
    for _ in range(n):
        if a > n//2:
            res.append(a)
        if b <= n//2:
            res.append(b)   
        a -= 1 
        b += 1

    print(" ".join(list(map(str,res))))