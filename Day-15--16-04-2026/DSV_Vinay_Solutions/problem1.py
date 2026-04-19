digs = []
nums = []
for i in range(9):
    tem2 = []
    tem1 = 0
    for j in range(9-i,10):
        tem1 += j
        tem2.append(j)
    nums.append(tem1)
    digs.append(tem2)

t = int(input())
for _ in range(t):
    x = int(input())

    if x >45:
        print(-1)
        continue


    for i,y in enumerate(nums):
        if x <= y:
            pos = i
            break
    
    findig = digs[pos]


    if pos == 0:
        print(x)
    else:
        findig[0] = x - nums[pos-1]
        print("".join(list(map(str,findig))))




             