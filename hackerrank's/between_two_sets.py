def getTotalX(a, b):
    elements = 0
    maxA=min(a)
    minB=min(b)
    taille_a= len(a)
    taille_b= len(b)
    for i in range(maxA,minB+1):
        is_in_set = True
        for j in range(taille_a):
            if i%a[j]!=0:
                is_in_set = False
                break 
        for k in range(taille_b):
            if b[k]%i!=0:
                is_in_set = False 
                break 
        if is_in_set==True:
            elements+=1
    return elements