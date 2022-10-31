def permutationEquation(p):
    p = [i-1 for i in p]
    n = len(p)
    a = list(range(n))
    t=[0]*n
    s=[0]*n
    for i in range(n):
        t[p[i]]=a[i]
    for j in range(n):
        s[p[j]]=t[j]
    for k in range(n):
        s[k]+=1
    return s