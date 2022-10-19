def viralAdvertising(n):
    shared = 5//2*3
    liked = 5//2
    for i in range(n-1):
        liked += shared //2
        shared = (shared//2) * 3
    return liked