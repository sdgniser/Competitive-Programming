for _ in range(int(input())):
    ar = list(input())
    k = 0
    for i in range(len(ar)):
        if i !=0 and  ar[i] != '0':
            k = i
            break
    

    
    # print(k)
    if k == 0:
        if int((''.join(ar[:1]))) < int((''.join(ar[1:]))):
            print(''.join(ar[:1]), (''.join(ar[1:])))
        else:
            print(-1)
    else:
        if int((''.join(ar[:k]))) < int((''.join(ar[k:]))):
            print(''.join(ar[:k]), (''.join(ar[k:])))
        else:
            print(-1)