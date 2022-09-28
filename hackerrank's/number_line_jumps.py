def kangaroo(x1, v1, x2, v2):
    pos1=x1
    pos2=x2
    for i in range(10000):
        pos1+=v1
        pos2+=v2
        if pos2==pos1:
            return "YES"
    return  "NO"