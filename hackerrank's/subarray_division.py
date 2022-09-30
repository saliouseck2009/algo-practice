def birthday(s, d, m):
    taille_s = len(s)
    return len({ i  for i in range(taille_s-m+1) if sum(s[i:i+m])==d})