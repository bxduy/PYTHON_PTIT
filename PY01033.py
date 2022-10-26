import math

n, k = [int(x) for x in input().split()]
for i in range(n, k-1):
    for j in range(i+1, k):
        if math.gcd(i, j) == 1:
            for z in range(j+1, k+1):
                if math.gcd(j, z) == 1:
                    if math.gcd(z, i) == 1:
                        print(f"({i}, {j}, {z})")