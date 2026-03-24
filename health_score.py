def calculate_score(stars, forks, issues):

    score = 0

    if stars > 100:
        score += 4

    if forks > 50:
        score += 3

    if issues < 100:
        score += 3

    return score