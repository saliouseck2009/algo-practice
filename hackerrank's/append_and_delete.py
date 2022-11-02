def appendAndDelete(s, t, k):
    len_t = len(t)
    len_s = len(s)
    common_letter = 0
    min_tab = min(len_s,len_t)
    for i in range(min_tab):
        if s[i]!=t[i]:
            break 
        else : 
            common_letter+=1
    move = len_s+len_t-2*common_letter if len_s>= len_t else len_t - common_letter  
    return "Yes" if len(s)+len(t) <= k or k>=move and (k-move)%2==0  else "No"