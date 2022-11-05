def cut_the_sticks(arr):
    lenght_after_cut=[]
    while len(arr)!=0:
        lenght_after_cut.append(len(arr))
        mini = min(arr)
        for i in range(len(arr)):
            arr[i]=arr[i]-mini
        arr = [i for i in arr if i >0]
    return lenght_after_cut 