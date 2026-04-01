t = int(input())
for _ in range(t):
    x,y = list(map(int, input().split()))
    flag = True
    if y>x+1:
        flag = False
    
    if (x-y)%9 != 8:
        flag = False
    
    if flag:
        print("YES")
    else:
        print("NO")
