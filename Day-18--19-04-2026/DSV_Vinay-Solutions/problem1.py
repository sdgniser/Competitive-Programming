for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    found = {}
    rep = False
    for i in ar:
        if i not in found:
            found[i] = 1
        else:
            rep = True
            break
    if rep:
        print("YES")
    else:
        if ar == sorted(ar,reverse=True):
            print("NO")
        else:
            print("YES")
