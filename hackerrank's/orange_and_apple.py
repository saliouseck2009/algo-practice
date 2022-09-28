def count_apples_and_oranges(s, t, a, b, apples, oranges):
    sam_orange = 0
    sam_apple = 0
    for i in range(len(oranges)):
        oranges[i]+=b
        if s<=oranges[i]<=t:
            sam_orange+=1
    for i in range(len(apples)):
        apples[i]+=a
        if s<=apples[i]<=t:
            sam_apple+=1
    print(sam_apple)
    print(sam_orange)
    