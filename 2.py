from sys import stdin

from computer import compute

p = [int(x) for x in stdin.readline().split(',')]

# part 1
print(compute(p.copy(), 12, 2))

# part 2
for n in range(0, 99):
    for v in range(0, 99):
        if compute(p.copy(), n, v) == 19690720:
            print(100 * n + v)
