import math
t = int(input())
for _ in range(t):
    ar1 = list(input())
    ar2 = list(input())
    def smallest_divisor(ar):
        for i in range(len(ar)):
            if ar[:i+1]*(len(ar)//(i+1)) == ar:
                return(ar[:i+1])
        
    a = smallest_divisor(ar1)
    b = smallest_divisor(ar2)
    if a == b:
        print("".join(a*math.lcm(len(ar1)//len(a),len(ar2)//len((b)))))
    else:
        print(-1)