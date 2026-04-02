t = int(input())
for _ in range(t):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))
    
    def maxer(ar):
        partial_sum = 0
        maxer = 0
        for i in ar:
            partial_sum += i
            if partial_sum > maxer:
                maxer = partial_sum
        return maxer
    
    # print(f"ans is :{maxer(blue)+maxer(red)}")
    print(maxer(red)+maxer(blue))
