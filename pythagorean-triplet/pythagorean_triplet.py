def triplets_with_sum(number):
    triplets = []
    for a in range(number//2):
        for b in range(a, number//2):
            c = number - a - b
            # print(a, b, c)
            if is_triplet([a, b, c]):
                triplets.append([a, b, c])
    return triplets


# def triplets_in_range(start, end):
#     pass


def is_triplet(triplet):
    return triplet[0]**2 + triplet[1]**2 == triplet[2]**2
