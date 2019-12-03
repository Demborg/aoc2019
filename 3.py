from sys import stdin

direction = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

def make_dict(row):
    place = 1
    pos = (0, 0)
    s = {}
    for move in row.split(','):
        for i in range(int(move[1:])):
            pos = tuple(p + d for p, d in zip(pos, direction[move[0]]))
            if not pos in s:
                s[pos] = place
            place+=1
    return s

s1 = make_dict(stdin.readline())
s2 = make_dict(stdin.readline())

intersecting_points = set(s1.keys()).intersection(s2.keys())

#p1
print(sorted(sum(abs(v) for v in t) for t in intersecting_points))

#p2
print(sorted(s1[p] +s2[p] for p in intersecting_points))




        
