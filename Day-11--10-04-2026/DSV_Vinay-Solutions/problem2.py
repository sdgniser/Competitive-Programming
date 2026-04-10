import math

n = int(input())
r = math.floor(math.log10(n))
bas = 10**r
closest = (n//bas)*bas
# print(bas)
# print(closest)

if n < 10:
    print(n)
else:
    for i in range(r+1):
        if i == 0:
            if closest + bas - 1 == n:
                print(n)
                break
        if (closest + bas - 1 - 10**i ) <= n:
            print(closest + bas - 1 - 10**i)
            break


