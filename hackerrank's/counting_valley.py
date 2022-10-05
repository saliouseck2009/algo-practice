def counting_valleys(steps, path):
    position = 0 
    old_pos = 0
    traversed_valleys= 0
    for i in path:
        old_pos=position
        if i=='U':
            position+=1
        else: 
            position-=1
        if position == 0 and old_pos==-1:
            traversed_valleys+=1
    return traversed_valleys