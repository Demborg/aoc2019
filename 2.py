from sys import stdin

def compute(p, n=0, v=0):
    p[1] = n
    p[2] = v
    i = 0
    while True:
        if p[i] == 99:
            break
        p[p[i+3]] = p[p[i+1]] + p[p[i+2]] if p[i] == 1 else p[p[i+1]] * p[p[i+2]]
        i += 4
    return p[0]


p = [int(x) for x in stdin.readline().split(',')]

# part 1
print(compute(p.copy(), 12, 2))

# part 2
for n in range(0, 99):
    for v in range(0, 99):
        if compute(p.copy(), n, v) == 19690720:
            print(100 * n + v)
