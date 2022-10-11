def hurdle_race(k, height):
    return 0 if max(height)<=k else max(height)-k