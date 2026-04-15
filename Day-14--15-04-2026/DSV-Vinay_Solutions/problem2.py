t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    ar = list(input())
    
    #getting pos of L and R
    # ---
    lefts = []
    rights = []
    
    for i in range(n):
        if ar[i] == "L":
            lefts.append(i)
        else:
            rights.append(i)
    # ---


    # list of partial sums 
    # ---
    psums = []
    tem = 0
    for i in range(n):
        tem += nums[i]
        psums.append(tem)
    # ---

    score = 0
    i = 0
    while i<(min(len(lefts),len(rights))) and lefts[i] < rights[-i-1]:
        score += psums[rights[-i-1]] - psums[lefts[i]] + nums[lefts[i]]
        i += 1
    
    print(score)

    

    




