def findDigits(n):
    return len([i for i in str(n) if int(i) != 0 and n%int(i)==0])