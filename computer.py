def compute(p, n=None, v=None):
    p[1] = n if n is not None else p[1]
    p[2] = v if v is not None else p[2]
    i = 0
    while p[i] != 99:
        s = str(p[i])
        op = int(s[-2:])
        modes = [int(v) for v in s[:-2]]
        modes.reverse()
        while len(modes) < 3:
            modes.append(0)

        if op == 1:
            args = [i+j+1 if modes[j] else p[i+j+1] for j in range(3)]
            p[args[2]] = p[args[1]] + p[args[0]]
            i += 4
        elif op == 2:
            args = [i+j+1 if modes[j] else p[i+j+1] for j in range(3)]
            p[args[2]] = p[args[1]] * p[args[0]]
            i += 4
        elif op == 3:
            p[p[i+1]] = int(input("plz gif input: "))
            i += 2
        elif op == 4:
            print(p[p[i+1]])
            i += 2
    return p[0]
        
