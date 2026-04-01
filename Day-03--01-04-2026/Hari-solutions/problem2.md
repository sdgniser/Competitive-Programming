Instead of simulating every possible rotation, we compute how many shifts does it take to match a specific number 


for every number $1 \leq x \leq n$  we find its index in permutation $a$ - $pos_a(x)$ and it's index in permutation $b$ - $pos_b(x)$

To align x, permutation b must be shifted $pos_a(x) - pos_b(x) \mod n$ positions

We then calculate shift required for all n elements and output max (the frequency array - shift_counts)
