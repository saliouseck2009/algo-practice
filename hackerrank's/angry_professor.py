def angryProfessor(k, a):
    return "YES" if k>len([i for i in a if i<=0 ]) else "NO"