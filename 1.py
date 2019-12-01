# 1a
print(sum(int(x) // 3 - 2 for x in open('inputs/1a.txt').readlines()))

# 1b
def fuel_mass(module_mass):
    m = int(module_mass) // 3 - 2
    if m <= 0:
        return 0
    return m + fuel_mass(m)

print(sum(fuel_mass(line) for line in open('inputs/1a.txt').readlines()))

