def sum_of_multiples(limit: int, multiples: list):
    if 0 in multiples:
        multiples.remove(0)
    combs = set(multiples)
    for elem1 in multiples:
        for elem2 in multiples:
            if elem1 != elem2 and elem1*elem2 not in combs and elem1*elem2 < limit:
                combs.add(elem1*elem2)

    sum_set = set()
    while combs:
        elem = combs.pop()
        upper_limit = limit//elem if limit % elem == 0 else limit//elem + 1
        for n in range(1, upper_limit):
            sum_set.add(n*elem)
    return sum(sum_set)
