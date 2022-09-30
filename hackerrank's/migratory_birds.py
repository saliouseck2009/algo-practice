def migratory_birds(arr):
    len_arr = len(arr)
    counter = [0]*5
    for i in range(len_arr):
        counter[arr[i]-1]+=1
    maxi = 0
    for i in range(len(counter)):
        if counter[i]>counter[maxi]:
            maxi = i
    return maxi+1