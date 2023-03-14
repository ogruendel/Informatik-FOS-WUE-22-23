import random

d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(0, 1000):
    v1 = random.randint(1, 6)
    v2 = random.randint(1, 6)

    d[v1] += 1
    d[v2] += 1

for k, i in d.items():
    print(k, i)
