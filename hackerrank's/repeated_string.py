def repeatedString(s, n):
    a_per_bloc = s.count('a')
    blocs = n//len(s)
    if n%len(s)==0:
        return blocs*a_per_bloc
    else: 
        return blocs*a_per_bloc+s[:n%len(s)].count('a')
