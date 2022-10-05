def getMoneySpent(keyboards, drives, b):
    maxi = -1
    taille_drive = len(drives)
    taille_keybord = len(keyboards)
    for i in range(taille_drive):
        for j in range(taille_keybord):
            purchase = keyboards[j]+drives[i]
            if purchase<=b and purchase>maxi:
                maxi = purchase
    return maxi