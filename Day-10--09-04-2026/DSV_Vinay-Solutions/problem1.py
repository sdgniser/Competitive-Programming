# functions 
def I():
    return (list(map(int,input().split())))

t = int(input())
for _ in range(t):
    n , h , m = I()
    ar = []
    k = (h*60) + m
    for _ in range(n):
        a,b = I()
        ar.append(((a*60)+b))
    
    fin = [(i-k)%1440 for i in ar]
    ans = min(fin)
    print(f"{(ans//60)} {ans%60}")


    
