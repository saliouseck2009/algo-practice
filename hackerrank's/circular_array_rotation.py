def circularArrayRotation(a, k, queries):
    taille_tab = len(a)
    copy_tab = a.copy()
    for i in range(taille_tab):
        a[(i+k)%taille_tab]=copy_tab[i]
    return [a[i] for i in queries]