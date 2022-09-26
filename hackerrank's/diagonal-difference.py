def diagonal_difference(arr):
    diag_asc =diag_desc =0
    tab_length =len(arr)
    for i in range(tab_length):
        for j in range(tab_length):
            if i==j :
                diag_asc+=arr[i][j]
            if j == tab_length-i-1:
                diag_desc +=arr[i][j]
    return abs(diag_asc-diag_desc)