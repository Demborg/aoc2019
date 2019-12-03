from sys import stdin

direction = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

def make_set(row):
    pos = (0, 0)
    s = set()
    for move in row.split(','):
        for i in range(int(move[1:])):
            pos = tuple(p + d for p, d in zip(pos, direction[move[0]]))
            s.add(pos)
    return s

#p1
s1 = make_set(stdin.readline())
s2 = make_set(stdin.readline())

print(sorted(sum(abs(v) for v in t) for t in s1.intersection(s2)))


        
