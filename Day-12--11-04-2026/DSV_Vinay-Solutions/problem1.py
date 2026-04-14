t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(input())
    dic = {}
    aux = []
    atoz = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    # print(f"a to z is :{atoz}")
    for i in ar:
        if i not in dic:
            dic[i] = 1
    # print(f"log of all seen letters: {dic}")
    for i in atoz:
        if i in dic and dic[i] == 1:
            aux.append(i)
    # print("auxillary array is: {aux}")

    for i,x in enumerate(aux):
        dic[x] = aux[-i-1]
    
    # print(f"updated dic is: {dic}")

    for i in range(n):
        ar[i] = dic[ar[i]]
    # print(f"final decoded: {ar}")
    print("".join(ar))
    