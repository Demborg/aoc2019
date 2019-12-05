print(len({
    s for s in (str(n) for n in range(240920, 789857))
    if any(2 == sum(s[i] == c for i in range(len(s))) for c in set(s))
    and all(int(s[i]) <= int(s[i+1]) for i in range(len(s) -1))
}))
