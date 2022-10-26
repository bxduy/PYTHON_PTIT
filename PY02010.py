while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(f"{min(arr)} {max(arr)}" if min(arr) != max(arr) else "BANG NHAU")