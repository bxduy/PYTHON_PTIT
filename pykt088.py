n = int(input())
prime = [1 for i in range(int(n ** (1/2)) + 1)]
p = 2

while p ** 2 <= n:
    if prime[p] == 1:
        for j in range(p ** 2, int(n ** (1 / 2)) + 1, p):
            prime[j] = 0
    p += 1
prime[0] = prime[1] = 0

cnt = 0
for i in range(2, int(n ** (1 / 2))):
    if prime[i] == 1:
        if i ** 8 <= n:
            cnt += 1
        for j in range(i + 1, int(n ** (1 / 2)) + 1):
            if prime[j] == 1:
                if i ** 2 * j ** 2 <= n:
                    cnt += 1
                else:
                    break
print(cnt)
