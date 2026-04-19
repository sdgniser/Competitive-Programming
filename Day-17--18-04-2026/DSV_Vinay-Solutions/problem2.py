
def find_mex(arr):
    found = [0]*n
    res = []
    curr_mex = 0
    for i,x in enumerate(arr):
        found[x] = 1
        if x == curr_mex:
            while curr_mex<(len(arr)) and found[curr_mex] != 0:
                curr_mex += 1
        res.append(curr_mex)
    return res


def solve():
    global n
    n = int(input())
    ar = list(map(int,input().split()))
    prefix_mexes = find_mex(ar)
    for i,x in enumerate(prefix_mexes):
        if x == prefix_mexes[-1]:
            if i == n-1:
                print(-1)
                break
            elif find_mex(ar[i+1:])[-1] == x:
                print(2)
                print(1,i+1)
                print(i+2,n)
            else:
                print(-1)
            break
    
t = int(input())
for _ in range(t):
    solve()

