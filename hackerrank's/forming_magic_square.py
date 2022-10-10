carre_magic_3 = [[[4,9,2],[3,5,7],[8,1,6]],
                [[2,7,6],[9,5,1],[4,3,8]],
                [[6,1,8], [7,5,3],[2,9,4]],
                [[8,3,4],[1,5,9],[6,7,2]],
                [[2,9,4],[7,5,3],[6,1,8]],
                [[6,7,2],[1,5,9],[8,3,4]],
                [[8,1,6],[3,5,7],[4,9,2]],
                [[4,3,8],[9,5,1],[2,7,6]]]

def forming_magic_square(s):
    costs = [0]*8
    index_cost = 0
    for carre in carre_magic_3:
        
        for i in range(3):
            for j in range(3):
                costs[index_cost]+=abs(s[i][j]-carre[i][j])
        index_cost+=1
    return min(costs)