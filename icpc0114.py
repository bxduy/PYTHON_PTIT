def isPrime(num):
    for i in num:
        if i != '2' and i != '3' and i != '5' and i != '7':
            return False
    num = int(num)
    for i in range(2, int(num ** 0.5) + 1, 1):
        if num % i == 0:
            return False
    return num > 1

for i in range(int(input())):
    num = input()
    print("Yes" if (isPrime(num) and isPrime(num[::-1])) else "No")