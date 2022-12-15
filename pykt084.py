t = int(input())
data = list()
for i in range(t):
    data.append(input())
cnt = 0
topic = ""
for i in data:
    if i != "" and topic != "":
        cnt += 1
    elif i == "":
        topic += ":"
        print(topic, cnt)
        topic = ""
        cnt = 0
    else:
        topic = i
if topic != "":
    topic += ":"
    print(topic, cnt)