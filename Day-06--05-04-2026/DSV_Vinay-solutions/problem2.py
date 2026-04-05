t = int(input())
for _ in range(t):
    q = int(input())

    def solve(n):
        if n in {1,2,3,5,7,11}:
            return -1
        if n%4 == 0 or n%4 == 2:
            return(n//4)
        if n%4 ==1 or n%4 == 3:
            return((n//4)-1)
        
    # print(f"ans is: {solve(q)}")
    print(solve(q))
        

    




# 0 mod4 -> n//4
# 1 mod4 -> 4k + 1 = 4(k-2) + 9 -> n//4 -1
# 2 mod4 -> 4(k-1) + 6 -> n//4
# 3 mod4 -> 4(k-3) + 6 + 9 -> n//4 -1