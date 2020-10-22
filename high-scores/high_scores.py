def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    tmp_scores = sorted(scores, reverse=True)
    return tmp_scores if len(tmp_scores) < 3 else tmp_scores[:3]
