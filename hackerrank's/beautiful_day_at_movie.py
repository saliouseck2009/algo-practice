def beautifulDays(i, j, k):
    return len({number for number in range(i,j+1)if (number - int(str(number)[-1::-1]) )%k==0 })