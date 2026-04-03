t = int(input())
for _ in range(t):
    n = int(input())
    ar1 = list(map(int, input().split()))
    
    def adj(ar):
        res = []
        for i,x in enumerate(ar):
            if x != 0:
                res.append(i)
                break
        for i,x in enumerate(ar[::-1]):
            if x != 0:
                res.append(n-i)
                break
        # print(f"trail removed we get:{ar[res[0]:res[1]]}")
        if 0 in ar[res[0]:res[1]]:
            return(2)
        return(1)

    def solve():
        if ar1 == [0]*n:
            return(0)
        if 0 in ar1:
            return(adj(ar1))  
        return(1)
    
    # print(f"answer is: {solve()}")
    print(solve())