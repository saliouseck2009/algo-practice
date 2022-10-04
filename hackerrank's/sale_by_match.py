def sock_merchant(n, ar):
    socks=set(ar)
    pairs= 0
    for i in socks:
        pairs = pairs + ar.count(i)//2
    return pairs