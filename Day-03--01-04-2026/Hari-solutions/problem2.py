n = int(input())

perm_a = list(map(int, input().split()))
perm_b = list(map(int, input().split()))

pos_a = [0]*(n+1)
pos_b = [0]*(n+1)

for i in range(n):
    pos_a[perm_a[i]] = i
    pos_b[perm_b[i]] = i

shift_counts = [0]*(n)

for x in range(1, n+1):
    shift = (pos_b[x] - pos_a[x]) % n
    shift_counts[shift] += 1


print(max(shift_counts))

