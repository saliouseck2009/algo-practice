def saveThePrisoner(n, m, s):
    result = (m+s-1)%n
    return n if result ==0 else result
   