print(len({
    s for s in (str(n) for n in range(240920, 789857))
    if len(set(s)) < 6 
    and all(int(s[i]) <= int(s[i+1]) for i in range(len(s) -1))
}))
