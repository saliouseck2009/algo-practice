def library_fine(d1, m1, y1, d2, m2, y2):
    if d1 <= d2 and m1 <= m2 and y1<=y2 or (y1<y2) or (m1<m2 and y1==y2) or (d1<d2 and m1==m2 and y1==y2):
        return 0
    elif y1!=y2:
        return 10000
    elif m1!=m2 :
        return  500*(m1-m2)
    elif d1!=d2 :
        return 15*(d1-d2)