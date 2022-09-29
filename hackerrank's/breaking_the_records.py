def breakingRecords(scores):
    min_s=max_s=scores[0]
    worst=best=0
    score_length=len(scores)
    for index in range(1,score_length): 
        if scores[index]> max_s:
            max_s=scores[index]
            best+=1
        elif scores[index]< min_s:
            min_s = scores[index]
            worst+=1
    
    return [best,worst]