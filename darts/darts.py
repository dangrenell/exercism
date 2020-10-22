def score(x, y):
    sq_dist = x**2 + y**2
    return 5*(sq_dist <= 1) + 4*(sq_dist <= 25) + (sq_dist <= 100)
