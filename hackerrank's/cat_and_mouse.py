def cat_and_mouse(x, y, z):
    if abs(x-z)>abs(y-z):
        return "Cat B"
    elif abs(x-z)<abs(y-z):
        return "Cat A"
    else:
        return "Mouse C"