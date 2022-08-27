f = open('')
n = int(f.readline())
length = []
value = []
k = 36
for i in range(n):
    x, y = map(int, f.readline().split())
    length.append(x)
    value.append(y // k if y % k == 0 else y // k + 1)
m = float('inf')
for i in range(n):
    s0 = length[i]
    m0 = 0
    for j in range(n):
        m0 += value[j] * abs(length[j] - s0)
    if m0 < m:
        m = m0
        count = i + 1
print(m)
