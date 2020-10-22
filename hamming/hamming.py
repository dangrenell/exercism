def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        return sum([s_a != s_b for s_a, s_b in zip(strand_a, strand_b)])
