test_cases = int(input())

for _ in range(test_cases):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x + 1 >= y and (x + 1 - y)%9 == 0:
        print("YES")
    else:
        print("NO")

