from sys import stdin

d = {body: center for center, body in (line.strip().split(')') for line in stdin.readlines())}

def orbits(body):
    return [body] + orbits(d[body]) if body in d else []

# part 1
print(sum(len(orbits(b)) for b in d.keys()))

# part 2
our_orbits = orbits('YOU')
santa_orbits = orbits('SAN')
common = set(santa_orbits).intersection(our_orbits)
print(min(our_orbits.index(b) + santa_orbits.index(b) -2 for b in common))

