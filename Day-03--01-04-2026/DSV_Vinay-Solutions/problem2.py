n = int(input())
def placer(ar):
    res = [0]*len(ar)
    for i,x in enumerate(ar):
        res[x-1] = i
    return res
ar1 = list(map(int, input().split()))
ar2 = list(map(int, input().split()))

fin = [0]*n
pl1 = placer(ar1)
pl2 = placer(ar2)
for i in range(n):
    fin[i] = pl1[i] - pl2[i]
fin = [(i%n) for i in fin]
dic = {}
for i in fin:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+= 1
m = 0
# print(dic)
for i,x in dic.items():
    if x > m:
        m = x 

print(m)
