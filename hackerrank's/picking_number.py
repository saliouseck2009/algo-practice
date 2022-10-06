def pickingNumbers(a):
    a.sort()
    max_taille = 0
    counter = 0
    pos = 0
    for i in range(len(a)-1):
        if abs(a[pos]-a[i+1])<=1:
            counter+=1
        else:
            pos = i+1
            counter = 0
        if counter>max_taille:
                max_taille = counter 
    return max_taille+1