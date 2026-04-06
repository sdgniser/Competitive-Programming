t = int(input())
for _ in range(t):
    n,a,b,c = list(map(int,input().split()))
    cur = n%(a+b+c)
    dks = (n//(a+b+c))*3
    # print(f"cur is: {cur}")
    # print(f"dks is: {dks}")
    def solve(cur,a,b,dks):
        if cur == 0:
            return dks
        if cur-a <= 0:
            return dks+1
        if cur-a-b<=0:
            return dks+2
        return dks + 3
    # print(f"ans is : {solve(cur,a,b,dks)}")
    print(solve(cur,a,b,dks))
