t = int(input())
for _ in range(t):
    n = int(input())
    ans = n**2 + (n**2)-1 + (n**2)-2 + (n**2) - n - 1

    if n == 1:
        print(1)
    elif n == 2:
        print(9)
    elif n < 5:
        print(ans)
    else:
        print(ans - (2*n) + n**2 -1 - (2*n))



# 1  2  3  4  5 
# 6  7  8  9  10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
