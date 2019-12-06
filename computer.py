def _make_args(s, args, p, i):
        modes = [int(v) for v in s]
        modes.reverse()
        while len(modes) < args:
            modes.append(0)
        return [i+j+1 if modes[j] else p[i+j+1] for j in range(args)]


def compute(p, n=None, v=None):
    p[1] = n if n is not None else p[1]
    p[2] = v if v is not None else p[2]
    i = 0
    while p[i] != 99:
        s = str(p[i])
        op = int(s[-2:])

        print(op, s)
        if op == 1:
            args = _make_args(s[:-2], 3, p, i)
            p[args[2]] = p[args[1]] + p[args[0]]
            i += 4
        elif op == 2:
            args = _make_args(s[:-2], 3, p, i)
            p[args[2]] = p[args[1]] * p[args[0]]
            i += 4
        elif op == 3:
            p[p[i+1]] = int(input("plz gif input: "))
            i += 2
        elif op == 4:
            print(p[p[i+1]])
            i += 2
        elif op == 5:
            args = _make_args(s[:-2], 2, p, i)
            print(args)
            if p[args[0]] != 0:
                i = p[args[1]]
            else:
                i += 2
            print(i)
        elif op == 6:
            args = _make_args(s[:-2], 3, p, i)
            if p[args[0]] == 0:
                i = p[args[1]]
            else:
                i += 2
        elif op == 7:
            args = _make_args(s[:-2], 3, p, i)
            p[args[2]] = 1 if p[args[0]] < p[args[1]] else 0
            i += 4
        elif op == 8:
            args = _make_args(s[:-2], 3, p, i)
            p[args[2]] = 1 if p[args[0]] > p[args[1]] else 0
            i += 4
        else:
            raise IndexError('Bad opcode')
    return p[0]
        
