import queue

n = int(input())
q = queue.Queue()
arr = ['2', '3', '5', '7']
for i in arr:
    q.put(i)
while not q.empty():
    first = q.get()
    if first[-1] != '2' and len(set(first)) == 4:
        print(first)
    for i in arr:
        if len(first) < n:
            q.put(first + i)