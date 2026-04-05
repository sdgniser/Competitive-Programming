t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    k = 0
    for i in range(n):
        if ar[i] == i+1+k:
            k += 1
    
    # print(f"ans is: {n+k}")
    print(n+k)

